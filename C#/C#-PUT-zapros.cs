// PUT запрос
string lgpass = project.Variables["lgpass"].Value;
lgpass = "Authorization: Basic " + lgpass;
string url = project.Variables["url"].Value;
string price = project.Variables["price"].Value;

var httpWebRequest = (HttpWebRequest)WebRequest.Create(url);
httpWebRequest.UserAgent =  "Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:46.0) Gecko/20100101 Firefox/46.0";
httpWebRequest.ContentType = "text/plain; charset=UTF-8";
httpWebRequest.Headers.Add(lgpass);
httpWebRequest.Method = "PUT";

using (var Writer = new StreamWriter(httpWebRequest.GetRequestStream()))
{
    string parametrs = "price=" + price;

    Writer.Write(parametrs);
    Writer.Flush();
    Writer.Close();
}

System.Net.HttpWebResponse response = (System.Net.HttpWebResponse)httpWebRequest.GetResponse();
string result = response.StatusCode.ToString();
return result;