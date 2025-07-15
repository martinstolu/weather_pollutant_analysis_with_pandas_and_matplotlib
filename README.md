# 🌍 Air Pollution Dashboard with Streamlit

This interactive dashboard visualizes air pollution trends (O3, NO2, VOC) over time across multiple countries using the [OpenAQ dataset](https://openaq.org/).

---

## 📦 Features

- 📈 Trend analysis of pollutants like **O₃**, **NO₂**, and **VOC**
- 🌐 Country-specific filtering
- 📊 Streamlit-powered interactive UI
- 🧼 Clean and grouped pollution data by **year**, **pollutant**, and **country**

---

## 📁 Project Structure

```
openaq.csv
main.py
README.md
```

---

## ⚙️ Setup & Run

1. **Install dependencies**:

```bash
pip install pandas matplotlib seaborn streamlit
```

2. **Run the app:**

```bash
streamlit run main.py
```

---

## 🧪 Data Preprocessing

- Input CSV: `openaq.csv` (semicolon `;` delimited)
- Parse and convert `Last Updated` column to datetime
- Extract `Year` from timestamps
- Filter only selected pollutants: `O3`, `NO2`, `VOC`
- Group data by `Country Code`, `Year`, and `Pollutant`, then compute average values

---

## 🖼️ Sample Visualization

Line plots of average pollutant values per year:

- Multiple country comparison
- Multi-pollutant trends
- Clean legend and styles via Seaborn

---

## 🎛️ Dashboard Features

- ✅ **Multiselect**: choose one or more countries
- ✅ **Multiselect**: choose pollutants to explore
- ✅ Dynamic plot updates
- ✅ Descriptive title and y-axis for pollutant values

---

## 🔍 Example Code Snippet

```python
fig, ax = plt.subplots(figsize=(10,6))
sns.lineplot(
    data=data, x='Year', y='Value',
    hue='Pollutant', style='Country Code',
    markers=True, ax=ax
)
st.pyplot(fig)
```

---

## 📚 References

- [OpenAQ Platform](https://openaq.org/)
- [Streamlit Docs](https://docs.streamlit.io/)
- [Seaborn Docs](https://seaborn.pydata.org/)
- [Pandas GroupBy](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html)

---

## 👨‍💻 Author

Built with ☁️ and 📊 by **Your Name Here**
