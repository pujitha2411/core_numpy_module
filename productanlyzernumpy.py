import numpy as np

class SalesAnalyzer:
    def __init__(self):  
        np.random.seed(42)

        
        self.months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                       'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        self.products = ['Product A', 'Product B', 'Product C']

        
        self.sales_data = np.random.randint(100, 500, size=(3, 12))


        seasonal_factor = np.array([0.8, 0.9, 1.0, 1.1, 1.2, 1.3,
                                    1.4, 1.3, 1.2, 1.1, 1.0, 0.9])
        self.sales_data = (self.sales_data * seasonal_factor).astype(int)

    def basic_stats(self):
        """Calculate and display basic statistics"""
        print("=== BASIC STATISTICS ===")
        total_sales = np.sum(self.sales_data)
        avg_monthly = np.mean(self.sales_data)
        std_monthly = np.std(self.sales_data)

        print(f"Total Sales: ${total_sales:,}")
        print(f"Average Monthly Sales: ${avg_monthly:.2f}")
        print(f"Standard Deviation: ${std_monthly:.2f}")

        # Per-product stats
        product_totals = np.sum(self.sales_data, axis=1)
        product_averages = np.mean(self.sales_data, axis=1)

        print("\nProduct Performance:")
        for i, product in enumerate(self.products):
            print(f"{product}: Total=${product_totals[i]:,}, Avg=${product_averages[i]:.2f}")

    def monthly_analysis(self):
        """Analyze monthly trends"""
        print("\n=== MONTHLY ANALYSIS ===")
        monthly_totals = np.sum(self.sales_data, axis=0)
        best_month_idx = np.argmax(monthly_totals)
        worst_month_idx = np.argmin(monthly_totals)

        print(f"Best Month: {self.months[best_month_idx]} (${monthly_totals[best_month_idx]:,})")
        print(f"Worst Month: {self.months[worst_month_idx]} (${monthly_totals[worst_month_idx]:,})")

        growth_rates = np.diff(monthly_totals) / monthly_totals[:-1] * 100
        avg_growth = np.mean(growth_rates)

        print(f"Average Monthly Growth Rate: {avg_growth:.2f}%")

    def product_comparison(self):
        """Compare performance metrics of products"""
        print("\n=== PRODUCT COMPARISON ===")
        product_metrics = {}

        for i, product in enumerate(self.products):
            data = self.sales_data[i]
            metrics = {
                'total': np.sum(data),
                'average': np.mean(data),
                'median': np.median(data),
                'std': np.std(data),
                'min': np.min(data),
                'max': np.max(data),
                'growth': (data[-1] - data[0]) / data[0] * 100
            }
            product_metrics[product] = metrics

        best_total = max(product_metrics.items(), key=lambda x: x[1]['total'])
        most_consistent = min(product_metrics.items(), key=lambda x: x[1]['std'])
        best_growth = max(product_metrics.items(), key=lambda x: x[1]['growth'])

        print(f"Highest Total Sales: {best_total[0]} (${best_total[1]['total']:,})")
        print(f"Most Consistent: {most_consistent[0]} (std: {most_consistent[1]['std']:.2f})")
        print(f"Best Growth: {best_growth[0]} ({best_growth[1]['growth']:.1f}%)")

    def forecasting(self):
        """Forecast next 3 months using linear regression"""
        print("\n=== FORECASTING ===")
        months_numeric = np.arange(12)

        for i, product in enumerate(self.products):
            coeffs = np.polyfit(months_numeric, self.sales_data[i], 1)
            trend_line = np.polyval(coeffs, months_numeric)

            future_months = np.arange(12, 15)
            forecast = np.polyval(coeffs, future_months)

            print(f"{product} Forecast (Next 3 months): "
                  f"${forecast[0]:.0f}, ${forecast[1]:.0f}, ${forecast[2]:.0f}")

            
            ss_res = np.sum((self.sales_data[i] - trend_line) ** 2)
            ss_tot = np.sum((self.sales_data[i] - np.mean(self.sales_data[i])) ** 2)
            r_squared = 1 - (ss_res / ss_tot)
            print(f"  Trend Fit (R²): {r_squared:.3f}")

    def correlation_analysis(self):
        """Display correlation between products"""
        print("\n=== CORRELATION ANALYSIS ===")
        correlation_matrix = np.corrcoef(self.sales_data)

        print("Product Correlations:")
        for i in range(len(self.products)):
            for j in range(i+1, len(self.products)):
                corr = correlation_matrix[i, j]
                print(f"{self.products[i]} vs {self.products[j]}: {corr:.3f}")

    def run_full_analysis(self):
        """Run complete dashboard analysis"""
        print("\nSALES ANALYSIS DASHBOARD")
        print("=" * 50)
        self.basic_stats()
        self.monthly_analysis()
        self.product_comparison()
        self.forecasting()
        self.correlation_analysis()

        print("\n=== RAW DATA ===")
        print("Sales Data (Products × Months):")
        print("Products:", self.products)
        print("Months:", self.months)
        print(self.sales_data)



analyzer = SalesAnalyzer()
analyzer.run_full_analysis()
