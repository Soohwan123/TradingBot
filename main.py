import abc_pattern_methods
import time
import matplotlib.pyplot as plt
import matplotlib.widgets as widgets
import bitcoin_price


print("This app is recommendedly used by traders who are familiar with Eliot's wave theory and have no self-control.")
print("It's a work in progress.")
print("Current version only supports 5 min timescale.")

fig, ax1 = plt.subplots()
fig.tight_layout()
ax1.set_xlabel('time (s)')
ax1.set_ylabel('price (USD)', color='tab:red')

price_list = []
time_list = []
volume_list = []
bitcoin_price.BitcoinPrice.generate_chart(price_list, time_list,volume_list, ax1, plt)
plt.ion()
plt.show()

# Add the button to the plot

lines = []
texts = []
abcButton_ax = plt.axes([0.05, 0.9, 0.1, 0.075])
abcButton = widgets.Button(abcButton_ax, 'Analyze ABC')

clearButton_ax = plt.axes([0.05, 0.7, 0.1, 0.075])
clearButton = widgets.Button(clearButton_ax, 'Clear')


def on_abcButton_clicked(event):
    xy = plt.ginput(2)
    startPointOfA = xy[0][1]
    endPointOfA = xy[1][1]

    threeEightTwoResult = abc_pattern_methods.AbcPatternMethods.Get_382_In_B_Wave(startPointOfA, endPointOfA)
    fiveResult = abc_pattern_methods.AbcPatternMethods.Get_5_In_B_Wave(startPointOfA, endPointOfA)
    sixOneEightResult = abc_pattern_methods.AbcPatternMethods.Get_618_In_B_Wave(startPointOfA, endPointOfA)

    # Perform calculations
    line1 = ax1.axhline(y=threeEightTwoResult, color='yellow', linestyle='--')
    lines.append(line1)
    text1 = ax1.text(0.05, threeEightTwoResult, f'382: {threeEightTwoResult:.2f}', color='yellow', transform=ax1.get_yaxis_transform(), ha='left', va='center')
    texts.append(text1)
    line2 = ax1.axhline(y=fiveResult, color='orange', linestyle='--')
    lines.append(line2)
    text2 = ax1.text(0.05, fiveResult, f'5: {fiveResult:.2f}', color='orange', transform=ax1.get_yaxis_transform(), ha='left', va='center')
    texts.append(text2)
    line3 = ax1.axhline(y=sixOneEightResult, color='red', linestyle='--')
    lines.append(line3)
    text3 = ax1.text(0.05, sixOneEightResult, f'618: {sixOneEightResult:.2f}', color='red', transform=ax1.get_yaxis_transform(), ha='left', va='center')
    texts.append(text3)
    
    plt.draw()

def on_clearButton_clicked(event):
    for line in lines:
        line.remove()
    lines.clear()

    for text in texts:
        text.remove()
    texts.clear()
    plt.draw()

clearButton.on_clicked(on_clearButton_clicked)
abcButton.on_clicked(on_abcButton_clicked)

while True:
    bitcoin_price.BitcoinPrice.update(0, price_list, time_list, volume_list, ax1, fig, plt)
    # limit update to every 5 minutes
    plt.draw()
    plt.pause(5)
    print("Updated")
