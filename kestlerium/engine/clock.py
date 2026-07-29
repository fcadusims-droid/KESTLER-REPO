"""O relógio do Kestlerium.

O mundo anda no tempo real do Brasil: se aqui são 21h de uma terça, no
Kestlerium são 21h da mesma terça e está de noite. Um tick são 30 minutos, e
`tick % TICKS_PER_DAY` corresponde exatamente à hora de Brasília porque a época
é fixada à meia-noite local.

Duas implementações, mesma interface:

  RealClock  — produção. Lê a hora de verdade.
  FastClock  — validação. Avança sob comando, para rodar 90 dias em segundos.

A validação PRECISA existir separada: o portão da Fase 3 mede 90 dias de
simulação, e esperar 90 dias reais para descobrir que a ontologia está errada
não é uma opção. Rodadas rápidas usam banco próprio e nunca tocam o mundo real.
"""

from __future__ import annotations

from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

TZ = ZoneInfo("America/Sao_Paulo")
TICK_MINUTES = 30
TICKS_PER_DAY = 24 * 60 // TICK_MINUTES  # 48

# Meia-noite local do dia em que o mundo começou. Fixar na meia-noite faz
# tick % 48 casar com a hora de Brasília sem nenhuma conversão.
#
# A época NÃO é constante de código: ela é decidida quando o mundo nasce e
# gravada em world_clock.epoch_iso. Se fosse recalculada a cada execução, a
# numeração dos ticks mudaria de um dia para o outro e o histórico inteiro se
# deslocaria — as chegadas dos personagens junto.
EPOCH = datetime.now(TZ).replace(hour=0, minute=0, second=0, microsecond=0)


def default_epoch() -> datetime:
    """Meia-noite de hoje em Brasília. Só usada quando o mundo é criado."""
    return datetime.now(TZ).replace(hour=0, minute=0, second=0, microsecond=0)


def set_epoch(moment: datetime) -> None:
    """Fixa a época do mundo (lida do banco na abertura)."""
    global EPOCH
    if moment.tzinfo is None:
        moment = moment.replace(tzinfo=TZ)
    EPOCH = moment.astimezone(TZ)


def tick_to_datetime(tick: int) -> datetime:
    return EPOCH + timedelta(minutes=TICK_MINUTES * tick)


def datetime_to_tick(moment: datetime) -> int:
    if moment.tzinfo is None:
        moment = moment.replace(tzinfo=TZ)
    delta = moment.astimezone(TZ) - EPOCH
    return int(delta.total_seconds() // (TICK_MINUTES * 60))


def time_of_day(tick: int) -> int:
    """Posição dentro do dia, 0..47. Tick 42 = 21:00."""
    return tick % TICKS_PER_DAY


def label(tick: int) -> str:
    return tick_to_datetime(tick).strftime("%d/%m/%Y %H:%M")


def is_night(tick: int) -> bool:
    hour = tick_to_datetime(tick).hour
    return hour >= 20 or hour < 6


class RealClock:
    """Produção: o mundo colado no relógio de Brasília."""

    mode = "real"

    def current_tick(self) -> int:
        return datetime_to_tick(datetime.now(TZ))

    def now(self) -> datetime:
        return datetime.now(TZ)


class FastClock:
    """Validação: avança sob comando, sem esperar o tempo passar."""

    mode = "rapido"

    def __init__(self, start_tick: int = 0) -> None:
        self._tick = start_tick

    def current_tick(self) -> int:
        return self._tick

    def advance(self, ticks: int = 1) -> int:
        self._tick += ticks
        return self._tick

    def set_tick(self, tick: int) -> None:
        self._tick = tick

    def now(self) -> datetime:
        return tick_to_datetime(self._tick)
