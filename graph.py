import pandas as pd
import matplotlib.pyplot as plt




#ARMOR

# Read CSV file into a DataFrame
df = pd.read_csv('csv/armor.csv', names=['Armor', 'Defense', 'Magic Defense', 'Materia Slots'])

# Plotting the graph
fig, ax = plt.subplots(figsize=(15, 10))

# Number of bars for each armor
num_bars = 3
bar_width = 0.25
bar_positions = range(len(df))

# Plotting bars for Defense, Magic Defense, and Materia Slots
ax.bar(bar_positions, df['Defense'], bar_width, label='Defense', color='blue')
ax.bar([p + bar_width for p in bar_positions], df['Magic Defense'], bar_width, label='Magic Defense', color='green')
ax.bar([p + 2 * bar_width for p in bar_positions], df['Materia Slots'], bar_width, label='Materia Slots', color='orange')

# Adding labels above each bar
for i, (defense, magic_defense, materia_slots) in enumerate(zip(df['Defense'], df['Magic Defense'], df['Materia Slots'])):
    ax.text(i, defense + 5, str(defense), ha='center', va='bottom')
    ax.text(i + bar_width, magic_defense + 5, str(magic_defense), ha='center', va='bottom')
    ax.text(i + 2 * bar_width, materia_slots + 5, str(materia_slots), ha='center', va='bottom')

# Adding labels and title
plt.ylabel('Stats')
plt.title('Comparison of Armor Stats')
plt.xticks([p + bar_width for p in bar_positions], df['Armor'], rotation=45)
plt.legend()

# Save plot as PNG
plt.savefig('images/comp_armor.png')


#WEAPONS


df = pd.read_csv('csv/weapon.csv', names=['User', 'Name', 'Style', 'Attack', 'Magic Attack', 'Defense', 'Magic Defense', 'HP', 'MP', 'Comments'])

# Filter the DataFrame to include only weapons used by Cloud
cloud_weapons = df[df['User'] == 'Cloud']

# Plotting the graph
fig, ax = plt.subplots(figsize=(15, 10))

# Number of bars for each weapon
num_bars = len(cloud_weapons)
bar_width = 0.15
bar_positions = range(num_bars)

# Plotting bars for each attribute
attributes = ['Attack', 'Magic Attack', 'Defense', 'Magic Defense']
colors = ['blue', 'green', 'red', 'orange']
for i, attr in enumerate(attributes):
    bars = ax.bar([p + i * bar_width for p in bar_positions], cloud_weapons[attr], bar_width, label=attr, color=colors[i])
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, height, str(height), ha='center', va='bottom')

# Adding labels and title
plt.ylabel('Stats')
plt.title('Cloud\'s Weapon Stats')
plt.xticks([p + 2 * bar_width for p in bar_positions], cloud_weapons['Name'], rotation=45, ha='right')
plt.legend()

plt.savefig('images/comp_cloud.png')











df = pd.read_csv('csv/weapon.csv', names=['User', 'Name', 'Style', 'Attack', 'Magic Attack', 'Defense', 'Magic Defense', 'HP', 'MP', 'Comments'])

# Filter the DataFrame to include only weapons used by Cloud
cloud_weapons = df[df['User'] == 'Tifa']

# Plotting the graph
fig, ax = plt.subplots(figsize=(15, 10))

# Number of bars for each weapon
num_bars = len(cloud_weapons)
bar_width = 0.15
bar_positions = range(num_bars)

# Plotting bars for each attribute
attributes = ['Attack', 'Magic Attack', 'Defense', 'Magic Defense']
colors = ['blue', 'green', 'red', 'orange']
for i, attr in enumerate(attributes):
    bars = ax.bar([p + i * bar_width for p in bar_positions], cloud_weapons[attr], bar_width, label=attr, color=colors[i])
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, height, str(height), ha='center', va='bottom')

# Adding labels and title
plt.ylabel('Stats')
plt.title('Tifa\'s Weapon Stats')
plt.xticks([p + 2 * bar_width for p in bar_positions], cloud_weapons['Name'], rotation=45, ha='right')
plt.legend()

plt.savefig('images/comp_tifa.png')












df = pd.read_csv('csv/weapon.csv', names=['User', 'Name', 'Style', 'Attack', 'Magic Attack', 'Defense', 'Magic Defense', 'HP', 'MP', 'Comments'])

# Filter the DataFrame to include only weapons used by Cloud
cloud_weapons = df[df['User'] == 'Barret']

# Plotting the graph
fig, ax = plt.subplots(figsize=(15, 10))

# Number of bars for each weapon
num_bars = len(cloud_weapons)
bar_width = 0.15
bar_positions = range(num_bars)

# Plotting bars for each attribute
attributes = ['Attack', 'Magic Attack', 'Defense', 'Magic Defense']
colors = ['blue', 'green', 'red', 'orange']
for i, attr in enumerate(attributes):
    bars = ax.bar([p + i * bar_width for p in bar_positions], cloud_weapons[attr], bar_width, label=attr, color=colors[i])
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, height, str(height), ha='center', va='bottom')

# Adding labels and title
plt.ylabel('Stats')
plt.title('Barret\'s Weapon Stats')
plt.xticks([p + 2 * bar_width for p in bar_positions], cloud_weapons['Name'], rotation=45, ha='right')
plt.legend()

plt.savefig('images/comp_barret.png')











df = pd.read_csv('csv/weapon.csv', names=['User', 'Name', 'Style', 'Attack', 'Magic Attack', 'Defense', 'Magic Defense', 'HP', 'MP', 'Comments'])

# Filter the DataFrame to include only weapons used by Cloud
cloud_weapons = df[df['User'] == 'Aerith']

# Plotting the graph
fig, ax = plt.subplots(figsize=(15, 10))

# Number of bars for each weapon
num_bars = len(cloud_weapons)
bar_width = 0.15
bar_positions = range(num_bars)

# Plotting bars for each attribute
attributes = ['Attack', 'Magic Attack', 'Defense', 'Magic Defense']
colors = ['blue', 'green', 'red', 'orange']
for i, attr in enumerate(attributes):
    bars = ax.bar([p + i * bar_width for p in bar_positions], cloud_weapons[attr], bar_width, label=attr, color=colors[i])
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, height, str(height), ha='center', va='bottom')

# Adding labels and title
plt.ylabel('Stats')
plt.title('Aerith\'s Weapon Stats')
plt.xticks([p + 2 * bar_width for p in bar_positions], cloud_weapons['Name'], rotation=45, ha='right')
plt.legend()

plt.savefig('images/comp_aerith.png')
