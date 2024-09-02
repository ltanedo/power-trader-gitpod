// esm
import pl from 'nodejs-polars';
import fetch from 'node-fetch';

// nodejs-polars-linux-x64-gnu
export const handler = async (event) => {
    // TODO implement

    var data = await get({
        url: "https://api.orats.io/datav2/snapshot/strikes15",
        params: {
          "token": "{YOUR_ORATS_KEY}",
          "tradeDate": "202008201130",
        },
    })
    
    const df = pl.DataFrame(flattenRecords(data));
    console.log(df);
  
    df.writeJSON('__data__/output.json')
    df.writeCSV('__data__/output.csv')
    df.writeParquet('__data__/output.parquet')

    const response = {
      statusCode: 200,
      body: JSON.stringify('Hello from Lambda!'),
    };

    return response;
  };


async function get({ url, params = {}, headers = {}, timeout = 60, DEBUG = false}) {
  console.log("hello")
  const queryString = Object.keys(params).map(key => `${key}=${params[key]}`).join('&');
  const fullUrl = `${url}?${queryString}`;

  if (DEBUG) {
    console.log(fullUrl)
    console.log(headers)
  }

  return fetch(fullUrl, {
    method: 'GET',
    headers: headers,
  })
    .then(response => {        
      if (response.headers.get('Content-Type').includes("application/json")) { 
        return response.json() 
      } 
      else { return response.text() }
    })
    .catch(error => {
      if (DEBUG) console.log(error)
      return {"error": error }
    });
}

function flattenRecords(records) {
  return records.map((record) => {
    const flattenedRecord = {};
    flattenObject(record, flattenedRecord, '');
    return flattenedRecord;
  });

  function flattenObject(obj, result, prefix) {
    for (const key in obj) {
      if (typeof obj[key] === 'object' && obj[key] !== null) {
        flattenObject(obj[key], result, prefix + key + '.');
      } else {
        result[prefix + key] = obj[key];
      }
    }
  }
}
