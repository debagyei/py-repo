import matplotlib.pyplot as plt

dates = ['2021-01-01', '2021-01-02', '2021-01-03']
prices = [100, 101, 99]

plt.plot(dates, prices, color='blue', linestyle='solid', marker='o', label='Stock Price')
plt.xlabel('Date')
plt.ylabel('Stock Price Over Time')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()