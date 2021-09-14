# pandas IO

pandas I/O API 提供了许多读写函数，读文件的函数命名类似于`pandas.read_csv()` 返回一个 pandas 对象。对应的输出函数类似于 `DataFrame.to_csv()`。下面列举了所有的I/O方法：

| 格式类型 | 格式                  | 读方法           | 写方法         |
| -------- | --------------------- | ---------------- | -------------- |
| text     | CSV                   | `read_csv`       | `to_csv`       |
| text     | Fixed-Width Text File | `read_fwf`       |                |
| text     | JSON                  | `read_json`      | `to_json`      |
| text     | HTML                  | `read_html`      | `to_html`      |
| text     | Local clipboard       | `read_clipboard` | `to_clipboard` |
|          | MS_Excel              | `read_excel`     | `to_excel`     |
| binary   | OpenDocument          | `read_excel`     |                |
| binary   | HDF5 Format           | `read_hdf`       | `to_hdf`       |
| binary   | Feather Format        | `read_feather`   | `to_feather`   |
| binary   | Parquet Format        | `read_parquet`   | `to_parquet`   |
| binary   | ORC Format            | `read_orc`       |                |
| binary   | Msgpack               | `read_msgpack`   | `to_msgpack`   |
| binary   | Stata                 | `read_stata`     | `to_stata`     |
| binary   | SAS                   | `read_sas`       |                |
| binary   | Python Pickle Format  | `read_pickle`    | `to_pickle`    |
| SQL      | SQL                   | `read_sql`       | `to_sql`       |
| SQL      | Google Big Query      | `read_gbq`       | `to_gbq`       |

