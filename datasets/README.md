# Glass Classification Dataset

##  Dataset Overview

This dataset contains samples of glass with their chemical composition and classification type. It is used for multi-class classification tasks to identify different types of glass based on their physical and chemical properties.

**Source:** [UCI Machine Learning Repository - Glass Dataset](https://www.kaggle.com/datasets/uciml/glass)

---

##  Dataset Statistics

- **Total Instances:** 214
- **Number of Attributes:** 10
- **Number of Classes:** 6
- **Missing Values:** None
- **Data Type:** Numerical (continuous values)

---

##  Attributes Description

The dataset contains the following features:

| # | Attribute Name | Type | Range | Description |
|---|---|---|---|---|
| 1 | **Refractive Index** | Float | 1.51115 - 1.53393 | The refractive index of the glass sample |
| 2 | **Sodium (Na)** | Float | 10.73 - 17.38 | Weight percent of sodium oxide |
| 3 | **Magnesium (Mg)** | Float | 0 - 4.49 | Weight percent of magnesium oxide |
| 4 | **Aluminum (Al)** | Float | 0.29 - 3.5 | Weight percent of aluminum oxide |
| 5 | **Silicon (Si)** | Float | 69.81 - 75.41 | Weight percent of silicon oxide |
| 6 | **Potassium (K)** | Float | 0 - 6.21 | Weight percent of potassium oxide |
| 7 | **Calcium (Ca)** | Float | 5.43 - 16.19 | Weight percent of calcium oxide |
| 8 | **Barium (Ba)** | Float | 0 - 3.15 | Weight percent of barium oxide |
| 9 | **Iron (Fe)** | Float | 0 - 0.51 | Weight percent of iron oxide |
| 10 | **Target Class** | Integer | 1 - 6 | Glass classification type |

---

## ️ Glass Classification Types

The dataset contains 6 different types of glass:

| Class | Type | Count | Description |
|-------|------|-------|---|
| **1** | Building Windows - Float Processed | 70 | Glass used in building windows with float processing |
| **2** | Building Windows - Non-Float Processed | 76 | Glass used in building windows without float processing |
| **3** | Vehicle Windows - Float Processed | 17 | Glass used in vehicle windows with float processing |
| **4** | Vehicle Windows - Non-Float Processed | 0 | Glass used in vehicle windows (not present in this dataset) |
| **5** | Containers | 13 | Glass used for containers and jars |
| **6** | Tableware | 9 | Glass used for dishes and tableware |

**Note:** Class 4 has no instances in this dataset, making it a 5-class problem in practice.

---
