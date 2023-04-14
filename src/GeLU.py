from matplotlib import pyplot as plt

plt.style.use('seaborn-v0_8')
plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams["font.size"] = 14
plt.rcParams['text.usetex'] = True


def plot():
    
    plt.figure(figsize=(12, 6))

    axis = plt.gca()
    plt.setp(axis.get_xticklabels(), fontsize=14)
    plt.setp(axis.get_yticklabels(), fontsize=14)

    plt.ylabel("Average Time Allocation [sec]")
    plt.xlabel("Vertex")

    x = np.linspace(-10, 10, 100)
    GeLU = lambda x: .5*
    height = [average_time_allocations[id - 1] for id in NODE_ORDERING]
    color = [NODES[id]['color'] for id in NODE_ORDERING]
    plt.line(x, height, color=color, hatch='//')

    for i in range(len(x)):
        plt.text(i, height[i] + 0.01, round(height[i], 2), ha='center', zorder=100)

    plt.tight_layout()
    plt.show()


def main():
    plot()


if __name__ == "__main__":
    main()