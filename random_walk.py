from random import choice
from matplotlib import pyplot as plt


class RandomWalk:
    """ 一个生成随机游走数据的类 """

    def __init__(self, num_points=5000):
        """ 初始化随机游走的属性 """
        self.num_points = num_points

        # 所有的随机游走起始于(0, 0)
        self.x_values = [0]
        self.y_values = [0]

    
    def fill_walk(self):
        """ 计算随机游走包含的点 """
        while len(self.x_values) < self.num_points:
            # 决定前进的方向以及距离
            x_direction = choice([-1, 1])
            x_distance = choice(range(5))
            x_step = x_direction * x_distance

            y_direction = choice([-1, 1])
            y_distance = choice(range(5))
            y_step = y_direction * y_distance

            # 拒绝原地踏步
            if x_step == 0 and y_step == 0:
                continue

            # 得出下一点的坐标
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

if __name__ == '__main__':
    rw = RandomWalk()
    rw.fill_walk()

    plt.style.use('classic')
    fig, ax = plt.subplots()
    point_nums = range(rw.num_points)

    ax.plot(rw.x_values, rw.y_values, linewidth=3)
    # ax.scatter(rw.x_values, rw.y_values, c=point_nums, cmap=plt.cm.Blues, edgecolors='none', s=15)
    # ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    # ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
    ax.set_aspect('equal')

    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()