import seaborn as sns
import matplotlib.pyplot as plt

class PlotUtils:
    @staticmethod
    def plot_confusion_matrix(cm, classes, title, cmap=plt.cm.Blues):
        sns.heatmap(cm, annot=True, fmt='d', cmap=cmap, xticklabels=classes, yticklabels=classes)
        plt.tight_layout()
        plt.title(f'Confusion Matrix of {title}')
        plt.ylabel('True labels')
        plt.xlabel('Predicted labels')
