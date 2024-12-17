---
title: "Statistical Model"
author: "Scott Townsend"
date: "December 16, 2024"

execute:
  keep-md: true

format:
  html:
    code-fold: true
    code-line-numbers: true
---



### Data & Libraries


::: {.cell}

```{.r .cell-code}
library(dplyr)
library(ggplot2)
library(readr)
library(tidyr)

data1 <- read.csv("Offender.csv")
data2 <- read.csv("Victim.csv")
data3 <- read.csv("Offender_ethnicity.csv")
data4 <- read.csv("Victim_ethnicity.csv")
data5 <- read.csv("Offender_race.csv")
data6 <- read.csv("Victim_race.csv")
data7 <- read.csv("Offender_sex.csv")
data8 <- read.csv("Victim_sex.csv")
data9 <- read.csv("Location.csv")
data10 <- read.csv("Relationship.csv")
data11 <- read.csv("Weapon.csv")
data12 <- read.csv("Offense.csv")

data7_long <- data7 %>%
  pivot_longer(
    cols = everything(),          
    names_to = "Sex",             
    values_to = "Count"           
  )

data8_long <- data8 %>%
  pivot_longer(
    cols = everything(),          
    names_to = "Sex",             
    values_to = "Count"           
  )
```
:::


# Visualizations of the Ages of Offenders and Victims


::: {.cell}

```{.r .cell-code}
# Offender Counts
ggplot(data1, aes(x = key, y = value, fill = value)) + 
  geom_bar(stat = "identity") +
  labs(title = "Offender Age Distribution", x = "Offender Age", y = "Count") +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))
```

::: {.cell-output-display}
![](Statistical_Model_files/figure-html/unnamed-chunk-2-1.png){width=1152}
:::

```{.r .cell-code}
# Victim Counts
ggplot(data2, aes(x = key, y = value, fill = value)) + 
  geom_bar(stat = "identity") +
  labs(title = "Victim Age Distribution", x = "Victim Age", y = "Count") +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))
```

::: {.cell-output-display}
![](Statistical_Model_files/figure-html/unnamed-chunk-2-2.png){width=1152}
:::
:::


# Visualizations of Ethnicity


::: {.cell}

```{.r .cell-code}
# Offender Ethnicity Counts
ggplot(data3, aes(x = key, y = value, fill = value)) + 
  geom_bar(stat = "identity") +
  labs(title = "Offender Ethnicity Distribution", x = "Ethnicity", y = "Count") +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))
```

::: {.cell-output-display}
![](Statistical_Model_files/figure-html/unnamed-chunk-3-1.png){width=1152}
:::

```{.r .cell-code}
# Victim Ethnicity Counts
ggplot(data4, aes(x = key, y = value, fill = value)) + 
  geom_bar(stat = "identity") +
  labs(title = "Victim Ethnicity Distribution", x = "Ethnicity", y = "Count") +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))
```

::: {.cell-output-display}
![](Statistical_Model_files/figure-html/unnamed-chunk-3-2.png){width=1152}
:::
:::


# Visualizations of Race


::: {.cell}

```{.r .cell-code}
# Offender Race Counts
ggplot(data5, aes(x = key, y = value, fill = value)) + 
  geom_bar(stat = "identity") +
  labs(title = "Offender Race Distribution", x = "Race", y = "Count") +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))
```

::: {.cell-output-display}
![](Statistical_Model_files/figure-html/unnamed-chunk-4-1.png){width=1152}
:::

```{.r .cell-code}
# Victim Race Counts
ggplot(data6, aes(x = key, y = value, fill = value)) + 
  geom_bar(stat = "identity") +
  labs(title = "Victim Race Distribution", x = "Race", y = "Count") +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))
```

::: {.cell-output-display}
![](Statistical_Model_files/figure-html/unnamed-chunk-4-2.png){width=1152}
:::
:::


# Visualizations of Sex


::: {.cell}

```{.r .cell-code}
# Offender sex
ggplot(data7_long, aes(x = Sex, y = Count, fill = Sex)) +
  geom_bar(stat = "identity") +
  labs(title = "Distribution of Offender Sex", x = "Sex", y = "Count") +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))
```

::: {.cell-output-display}
![](Statistical_Model_files/figure-html/unnamed-chunk-5-1.png){width=1152}
:::

```{.r .cell-code}
# Victim sex
ggplot(data8_long, aes(x = Sex, y = Count, fill = Sex)) +
  geom_bar(stat = "identity") +
  labs(title = "Distribution of Victim Sex", x = "Sex", y = "Count") +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))
```

::: {.cell-output-display}
![](Statistical_Model_files/figure-html/unnamed-chunk-5-2.png){width=1152}
:::
:::


# Visualizations of Location


::: {.cell}

```{.r .cell-code}
# Location of Incidents
ggplot(data9, aes(x = key, y = value, fill = value)) +
  geom_bar(stat = "identity") +
  labs(title = "Incidents by Location", x = "Location", y = "Count") +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))
```

::: {.cell-output-display}
![](Statistical_Model_files/figure-html/unnamed-chunk-6-1.png){width=1152}
:::
:::


# Visualizations of Weapons used


::: {.cell}

```{.r .cell-code}
# Weapons used at Incident
ggplot(data11, aes(x = key, y = value, fill = value)) +
  geom_bar(stat = "identity") +
  labs(title = "Incidents by Weapon", x = "Weapon", y = "Count") +
  theme(axis.text.x = element_text(angle = 45, hjust =1))
```

::: {.cell-output-display}
![](Statistical_Model_files/figure-html/unnamed-chunk-7-1.png){width=1152}
:::
:::


# Visualizations of Offense


::: {.cell}

```{.r .cell-code}
# Type of Offense
ggplot(data12, aes(x = key, y = value, fill = value)) +
  geom_bar(stat = "identity") +
  coord_flip() +
  labs(title = "Type of Offense", x= "Offense", y = "Count") +
  theme(axist.text.x = element_text(angle = 45, hjust =1))
```

::: {.cell-output-display}
![](Statistical_Model_files/figure-html/unnamed-chunk-8-1.png){width=2112}
:::
:::


# Visualizations of Relationship between Offender and Victim


::: {.cell}

```{.r .cell-code}
# Relationship between Offender and Victim
ggplot(data10, aes(x = key, y = value, fill = value)) +
  geom_bar(stat = "identity") +
  coord_flip() +
  labs(title = "Relationship Between Offender and Victim", x = "Relationship", y = "Count")
```

::: {.cell-output-display}
![](Statistical_Model_files/figure-html/unnamed-chunk-9-1.png){width=1152}
:::
:::
