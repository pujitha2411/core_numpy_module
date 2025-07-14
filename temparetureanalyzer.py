import numpy as np

np.random.seed(0)
days = np.arange(1, 366)
temperatures = np.random.normal(loc=30, scale=5, size=365)

avg_temp = np.mean(temperatures)
min_temp = np.min(temperatures)
max_temp = np.max(temperatures)
std_dev = np.std(temperatures)
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

months = np.array_split(temperatures, 12)
monthly_stats = []
for i, month in enumerate(months):
    month_avg = np.mean(month)
    month_max = np.max(month)
    month_min = np.min(month)
    monthly_stats.append((i+1, month_avg, month_max, month_min))


z_scores = (temperatures - avg_temp) / std_dev
outlier_days = days[np.abs(z_scores) > 2]  


stable_days = days[np.round(temperatures, 1) == round(avg_temp, 1)]


top5_hot_days = days[np.argsort(temperatures)[-5:]][::-1]
top5_cold_days = days[np.argsort(temperatures)[:5]]

rolling_avg = np.convolve(temperatures, np.ones(7)/7, mode='valid')
hottest_week = np.argmax(rolling_avg) + 1
coldest_week = np.argmin(rolling_avg) + 1


range_20_25 = np.sum((temperatures >= 20) & (temperatures < 25))
range_25_30 = np.sum((temperatures >= 25) & (temperatures < 30))
range_30_35 = np.sum((temperatures >= 30) & (temperatures < 35))
range_35_40 = np.sum((temperatures >= 35) & (temperatures < 40))


above_avg_mask = temperatures > avg_temp
above_avg_days = np.sum(above_avg_mask)

print("====== WEATHER DATA ANALYZER (NUMPY ONLY) ======\n")
print(f" Yearly Avg Temp: {avg_temp:.2f}°C")
print(f" Lowest Temp: {min_temp:.2f}°C on Day {coldest_day}")
print(f" Highest Temp: {max_temp:.2f}°C on Day {hottest_day}")
print(f" Std Deviation: {std_dev:.2f}")
print(f" Temp Range: {temp_range:.2f}°C\n")

print(f" Heatwave Days (>38°C): {len(heatwave_days)} → {heatwave_days.tolist()}")
print(f" Cold Days (<20°C): {len(cold_days)} → {cold_days.tolist()}\n")

print(" Percentiles:")
print(f"  10th: {p10:.2f}°C | 25th: {p25:.2f}°C | 50th: {p50:.2f}°C")
print(f"  75th: {p75:.2f}°C | 90th: {p90:.2f}°C\n")

print(" Monthly Summary (Month | Avg | Max | Min):")
for m, avg, high, low in monthly_stats:
    print(f"  Month {m:02d}: Avg={avg:.2f}°C, Max={high:.2f}°C, Min={low:.2f}°C")

print("\n Temperature Range Distribution:")
print(f"  20–25°C: {range_20_25} days")
print(f"  25–30°C: {range_25_30} days")
print(f"  30–35°C: {range_30_35} days")
print(f"  35–40°C: {range_35_40} days\n")

print(f" Above Avg Days: {above_avg_days} days")
print(f" Stable Days (≈Avg): {len(stable_days)} → {stable_days.tolist()}")
print(f" Outlier Days (>|2σ|): {len(outlier_days)} → {outlier_days.tolist()}\n")

print(f" Top 5 Hottest Days: {top5_hot_days.tolist()}")
print(f" Top 5 Coldest Days: {top5_cold_days.tolist()}")
print(f" Hottest 7-Day Period Starts on Day: {hottest_week}")
print(f" Coldest 7-Day Period Starts on Day: {coldest_week}")
