# Feature-Selection
In this project I have done feature selection on semi-conductor dataset.

### In my recent data analysis project aimed at optimizing semiconductor manufacturing processes, I employed a comprehensive feature selection strategy using various filter-based techniques. Here's a brief summary:

## Duplicate Column Removal:
The initial dataset contained 592 columns, some of which were duplicates. Removing these duplicate columns helped streamline the dataset and eliminate redundant information.

## Variance Thresholding: 
Following duplicate column removal, I applied variance thresholding to identify and eliminate features with low variance. By setting a threshold of 0.05, I removed features that exhibited little variation, further refining the dataset.

## Correlation Filtering: 
Next, I examined the correlation between features to identify highly correlated pairs. Features with a correlation coefficient above 0.95 were considered redundant and subsequently removed. This step further pruned the dataset, focusing on independent and informative features.

## ANOVA (Analysis of Variance): 
Finally, I utilized ANOVA to select the top 100 features that exhibited the strongest association with the target variable. This statistical method helped identify features that contributed significantly to the variability in the target variable.

After applying these feature selection techniques, I trained and tested my model using the refined dataset containing only the selected features. The accuracy of the model significantly improved from 84% when using all 592 columns to 91% after feature selection.

This holistic approach to feature selection not only improved model performance but also streamlined the dataset, making it more interpretable and actionable for semiconductor manufacturing optimization.
