import numpy as np
from scipy.stats import binom


def get_stat_power(N, mu_h0, mu_h1, alpha):
    """
    Функция из методички Академии Аналитиков Авито.
    Вычисляет статистическую мощность критерия для биномиального распределения.

    Параметры
    ---------
    N : int или array-like
        Размер выборки (число испытаний).
    mu_h0 : float
        Вероятность успеха в нулевой гипотезе.
    mu_alternative : float
        Вероятность успеха при альтернативе.
    alpha : float
        Уровень значимости.

    Возвращает
    ----------
    power : float или np.ndarray
        Мощность критерия для каждого N.
    """
    N = np.asarray(N)

    binom_h0 = binom(n=N, p=mu_h0)
    binom_h1 = binom(n=N, p=mu_h1)

    # критическое значение: минимальное k, при котором P(X >= k | H0) <= alpha
    critical_value = binom_h0.ppf(1 - alpha) + 1

    # мощность = P(X >= critical_value | H1)
    power = 1 - binom_h1.cdf(critical_value - 1)

    return power
