import duckdb


def run_basic_queries(file_path):
    con = duckdb.connect()

    total_sales = con.execute(f"""
        SELECT SUM(Sales) AS total_sales
        FROM read_csv_auto('{file_path}')
    """).fetchone()[0]

    total_profit = con.execute(f"""
        SELECT SUM(Profit) AS total_profit
        FROM read_csv_auto('{file_path}')
    """).fetchone()[0]

    top_categories_raw = con.execute(f"""
        SELECT Category, SUM(Sales) AS total_sales
        FROM read_csv_auto('{file_path}')
        GROUP BY Category
        ORDER BY total_sales DESC
    """).fetchall()

    top_regions_raw = con.execute(f"""
        SELECT Region, SUM(Sales) AS total_sales
        FROM read_csv_auto('{file_path}')
        GROUP BY Region
        ORDER BY total_sales DESC
    """).fetchall()

    top_categories = {
        category: round(float(total_sales), 2)
        for category, total_sales in top_categories_raw
    }

    top_regions = {
        region: round(float(total_sales), 2)
        for region, total_sales in top_regions_raw
    }

    return {
        "total_sales": round(float(total_sales), 2),
        "total_profit": round(float(total_profit), 2),
        "top_categories": top_categories,
        "top_regions": top_regions,
    }


if __name__ == "__main__":
    results = run_basic_queries("data/raw/superstore.csv")

    print("SQL Results:")
    print(results)