// esm
import pl from 'nodejs-polars';
// import pl from 'polars';clear

// nodejs-polars-linux-x64-gnu
export const handler = async (event) => {
    // TODO implement

    const df = pl.DataFrame(
        {
            A: [1, 2, 3, 4, 5],
            fruits: ["banana", "banana", "apple", "apple", "banana"],
            B: [5, 4, 3, 2, 1],
            cars: ["beetle", "audi", "beetle", "beetle", "beetle"],
        }
    )
    let new_df = df.sort("fruits").select(
        "fruits",
        "cars",
        pl.lit("fruits").alias("literal_string_fruits"),
        pl.col("B").filter(pl.col("cars").eq(pl.lit("beetle"))).sum(),
        pl.col("A").filter(pl.col("B").gt(2)).sum().over("cars").alias("sum_A_by_cars"),
        pl.col("A").sum().over("fruits").alias("sum_A_by_fruits"),
        pl.col("A").reverse().over("fruits").flatten().alias("rev_A_by_fruits")
    )

    console.log(new_df)

    const response = {
      statusCode: 200,
      body: JSON.stringify('Hello from Lambda!'),
    };

    return response;
  };
  

// handler()