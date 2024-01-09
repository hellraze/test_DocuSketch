import os
import matplotlib.pyplot as plt

class PlotDrawer:
    def draw_plots(self, df):

        os.makedirs('plots', exist_ok=True)

        df.plot(x='gt_corners', y='rb_corners', kind='scatter')
        plot_path = 'plots/corners_comparison.png'
        plt.savefig('plots/corners_comparison.png')
        plt.close()
        return plot_path
