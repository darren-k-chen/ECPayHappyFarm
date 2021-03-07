using System.IO; using System.Net; using UnityEngine;

public class Reset : MonoBehaviour
{   // Author: Darren K.J. Chen, Ming Chuan University
    void Start() { } void Update() { } public void reset() {
        string API_METHOD = "/INIT";
        var httpWebRequest = (HttpWebRequest)WebRequest.Create(LandHandler.API_SERVER_NAME + API_METHOD);
        httpWebRequest.Method = "GET"; var httpResponse = (HttpWebResponse)httpWebRequest.GetResponse();
        string tmp; using (var streamReader = new StreamReader(httpResponse.GetResponseStream()))
        { tmp = streamReader.ReadToEnd(); } print(LandHandler.API_SERVER_NAME + API_METHOD + "\t" + tmp);
    } private void OnMouseDown() { onClick(); } void onClick() { reset(); }
}
