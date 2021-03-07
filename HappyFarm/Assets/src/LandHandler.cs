using System.IO; using System.Net; using UnityEngine;

public class LandHandler : MonoBehaviour
{   // Author: Darren K.J. Chen, Ming Chuan University
    public uint balance = 0;
    public SpriteRenderer spriteRenderer; public Sprite[] spriteArray;
    public static string logisticsStatus = "-1"; bool canCrop = false;
    public static string API_SERVER_NAME = "http://api.happyfarm.darren-cv.site";
    public void updateLogisticsStatus() {
        string API_METHOD = "/getLogisticsStatus";
        var httpWebRequest = (HttpWebRequest)WebRequest.Create(API_SERVER_NAME + API_METHOD);
        httpWebRequest.Method = "GET"; var httpResponse = (HttpWebResponse)httpWebRequest.GetResponse();
        using (var streamReader = new StreamReader(httpResponse.GetResponseStream()))
        { logisticsStatus = streamReader.ReadToEnd(); } print(API_SERVER_NAME + API_METHOD);
    } void changeSprite(Sprite newSprite) { spriteRenderer.sprite = newSprite; }
    private void OnMouseDown() { onClick(); } void onClick() {
        if (canCrop) { changeSprite(spriteArray[3]); balance++; updateBalance(balance); canCrop = false; return; }
        updateLogisticsStatus(); if (logisticsStatus == "3024") { changeSprite(spriteArray[1]); }
        else if (logisticsStatus == "300" )  { canCrop = false ;  changeSprite(spriteArray[0]); }
        else if (logisticsStatus == "3022")  { canCrop = true  ;  changeSprite(spriteArray[2]); }
        else changeSprite(spriteArray[3]); print(logisticsStatus); print(canCrop);
    } void Update() { } public void updateBalance(uint balance) {
        GameObject.Find("balanceHint").GetComponent<TextMesh>().text = balance.ToString();
    } void Start() { spriteRenderer = gameObject.GetComponent<SpriteRenderer>(); onClick(); }
}
