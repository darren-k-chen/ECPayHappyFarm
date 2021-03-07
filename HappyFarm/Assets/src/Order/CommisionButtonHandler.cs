using System.IO; using System.Net; using UnityEngine; using UnityEngine.SceneManagement;

public class CommisionButtonHandler : MonoBehaviour
{   // Author: Darren K.J. Chen, Ming Chuan University
    public void createOrder() {
        string API_METHOD = "/createShippingOrder";
        var httpWebRequest = (HttpWebRequest)WebRequest.Create(LandHandler.API_SERVER_NAME + API_METHOD);
        httpWebRequest.ContentType = "application/json"; httpWebRequest.Method = "POST";
        using (var streamWriter = new StreamWriter(httpWebRequest.GetRequestStream())) {
            string json = "{ \"GoodsAmount\": \"88\", \"CollectionAmount\": \"88\", \"GoodsName\": \"Carrot\", \"ReceiverName\": \"Darren\" }";
            print("[POST] " + json + "\n[TO] " + LandHandler.API_SERVER_NAME + API_METHOD); streamWriter.Write(json);
        } var httpResponse = (HttpWebResponse)httpWebRequest.GetResponse();
        using (var streamReader = new StreamReader(httpResponse.GetResponseStream())) print(streamReader.ReadToEnd());
    } public void queryLogisticsInfo() {
        string API_METHOD = "/queryLogisticsInfo";
        var httpWebRequest = (HttpWebRequest)WebRequest.Create(LandHandler.API_SERVER_NAME + API_METHOD);
        httpWebRequest.ContentType = "application/json"; httpWebRequest.Method = "POST";
        using (var streamWriter = new StreamWriter(httpWebRequest.GetRequestStream()))
        { string json = "{ \"AllPayLogisticsID\": \"1690205\" }"; streamWriter.Write(json); }
        var httpResponse = (HttpWebResponse)httpWebRequest.GetResponse();
        using (var streamReader = new StreamReader(httpResponse.GetResponseStream())) print(streamReader.ReadToEnd());
    } void onClick() { SceneManager.LoadScene(5); createOrder(); queryLogisticsInfo(); }
    private void OnMouseDown() { onClick(); } void Start() { } void Update() { }
}
