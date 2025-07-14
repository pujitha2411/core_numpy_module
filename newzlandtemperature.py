import numpy as np


np.random.seed(0)
days = np.arange(1, 366)
temperatures = np.random.normal(loc=20, scale=10, size=365)

avg_temp = np.mean(temperatures)
min_temp = np.min(temperatures)
max_temp = np.max(temperatures)
std_dev = np.std(temperatures)
var_temp = np.var(temperatures)
temp_range = max_temp - min_temp

hottest_day = np.argmax(temperatures) + 1
coldest_day = np.argmin(temperatures) + 1


heatwave_days = days[temperatures > 38]
cold_days = days[temperatures < 20]


p10 = np.percentile(temperatures, 10)
p25 = np.percentile(temperatures, 25)
p50 = np.percentile(temperatures, 50)
p75 = np.percentile(temperatures, 75)
p90 = np.percentile(temperatures, 90)
iqr = p75 - p25


months = np.array_split(temperatures, 12)
monthly_stats = []
for i, month in enumerate(months):
    month_avg = np.mean(month)
    month_max = np.max(month)
    month_min = np.min(month)
    monthly_stats.append((i+1, month_avg, month_max, month_min))


z_scores = (temperatures - avg_temp) / std_dev
outlier_days = days[np.abs(z_scores) > 2]


rounded = np.round(temperatures)
(unique, counts) = np.unique(rounded, return_counts=True)
mode_temp = unique[np.argmax(counts)]


rolling_avg = np.convolve(temperatures, np.ones(7)/7, mode='valid')
hottest_week = np.argmax(rolling_avg) + 1
coldest_week = np.argmin(rolling_avg) + 1


bins = [0, 20, 25, 30, 35, 40, 50]
labels = np.digitize(temperatures, bins)


above_avg_mask = temperatures > avg_temp
stable_days = days[np.round(temperatures, 1) == round(avg_temp, 1)]


day_diff = np.diff(temperatures)
max_rise = np.max(day_diff)
max_fall = np.min(day_diff)


top5_days = days[np.argsort(temperatures)[-5:]][::-1]
bottom5_days = days[np.argsort(temperatures)[:5]]


cumulative_sum = np.cumsum(temperatures)
cumulative_avg = cumulative_sum / days


cleaned_temperatures = np.where(temperatures > 45, avg_temp, temperatures)


first_hot_day = days[temperatures > 37][0] if np.any(temperatures > 37) else None

print("====== WEATHER DATA ANALYZER (NUMPY ONLY) ======\n")
print(f" Yearly Avg Temp: {avg_temp:.2f}°C")
print(f" Lowest Temp: {min_temp:.2f}°C on Day {coldest_day}")
print(f" Highest Temp: {max_temp:.2f}°C on Day {hottest_day}")
print(f" Std Dev: {std_dev:.2f} | Variance: {var_temp:.2f}")
print(f" Temp Range: {temp_range:.2f}°C | IQR: {iqr:.2f}°C\n")

print(f" Heatwave Days (>38°C): {len(heatwave_days)} → {heatwave_days.tolist()}")
print(f" Cold Days (<20°C): {len(cold_days)} → {cold_days.tolist()}")
print(f" Stable Days (≈Avg): {len(stable_days)} → {stable_days.tolist()}")
print(f" Outlier Days (>2σ): {len(outlier_days)} → {outlier_days.tolist()}")
print(f" Mode Temp (approx): {mode_temp}°C\n")

print(" Percentiles:")
print(f"  10th: {p10:.2f}°C | 25th: {p25:.2f}°C | 50th: {p50:.2f}°C | 75th: {p75:.2f}°C | 90th: {p90:.2f}°C")

print("\n Monthly Summary (Month | Avg | Max | Min):")
for m, avg, high, low in monthly_stats:
    print(f"  Month {m:02d}: Avg={avg:.2f}°C, Max={high:.2f}°C, Min={low:.2f}°C")

print("\n Temperature Differences Between Days:")
print(f"  Max Single-Day Rise: {max_rise:.2f}°C")
print(f"  Max Single-Day Fall: {max_fall:.2f}°C")

print("\n Top & Bottom 5 Days:")
print(f"  Top 5 Hottest Days: {top5_days.tolist()}")
print(f"  Bottom 5 Coldest Days: {bottom5_days.tolist()}")

print(f"\n First Day Above 37°C: Day {first_hot_day}" if first_hot_day else "No day crossed 37°C")
print(f" Hottest 7-Day Period Starts on Day: {hottest_week}")
print(f" Coldest 7-Day Period Starts on Day: {coldest_week}")

print(f"\n Cleaned Data (replaced >45°C with Avg): {np.any(temperatures != cleaned_temperatures)}")
