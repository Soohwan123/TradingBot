import abc_pattern_methods
import time
import matplotlib.pyplot as plt
import bitcoin_price

print("This app is recommendedly used by traders who are familiar with Eliot's wave theory and have no self-control.")
print("It's a work in progress.")
print("Current version only supports 5 min timescale.")

# selectedCrypto = input("Please enter the cryto you wanna analyse(1 = BTC, 2 = ETH")
# direction = input("Select your trading mode(1 = long, 2 = short")

# currentWave = input("Enter the current wave you analyzed(1 = B, 2 = C)  :  ")
# startPointOfA = float(input("Enter the start point of your analysed A wave  :  "))
# endPointOfA = float(input("Enter the end point of your analysed A wave  :  "))

fig, ax1 = plt.subplots()
fig.tight_layout()
ax1.set_xlabel('time (s)')
ax1.set_ylabel('price (USD)', color='tab:red')

price_list = []
time_list = []
bitcoin_price.BitcoinPrice.generate_chart(price_list, time_list, ax1)

plt.show()
while True:
    bitcoin_price.BitcoinPrice.update(0, price_list, time_list, ax1, fig, plt)
    # limit update to every 5 minutes
    time.sleep(10)

    # check if the latest price is out of view and move the view to the right if necessary
    xlim = ax1.get_xlim()
    if float(time_list[-1]) > float(xlim[1]):
        ax1.set_xlim(xlim[0], xlim[1] + 300)
    fig.canvas.draw()
    print("updated")
    plt.show()



# flag = True
# while flag:
#     price = bitcoin_price.coins[0]['quote']['USD']['price']
    
#     print(price)
#     print(abc_pattern_methods.Get_382_In_B_Wave(startPointOfA, endPointOfA))
#     print(abc_pattern_methods.Get_5_In_B_Wave(startPointOfA, endPointOfA))
#     print(abc_pattern_methods.Get_618_In_B_Wave(startPointOfA, endPointOfA))
    
#     for wave_percentage, suggestion in [(0.382, "mildly"), (0.5, "moderately"), (0.618, "strongly")]:
#         wave_price = abc_pattern_methods.Get_Recommended_Price(startPointOfA, endPointOfA, wave_percentage)
#         if (price <= wave_price * 1.001 and price >= wave_price * 0.999):
#             print(f"We {suggestion} suggest you to buy/sell now")
#             break
    
#     # Sleep for 5 minutes (5 * 60 seconds)
#     time.sleep(5 * 60)