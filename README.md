# ECPay Competition Team Prototype Reference
## 產品發想：開心農場
### 一、產品特色：本遊戲透過「競價模式」串接金流，提供作物集合競價的平台，使得賣方能夠脫離盤商剝削，買方也能獲取公平之價格，創造買賣雙方雙贏，並將「作物成長」結合作物運送之物流，依據物流狀態來決定作物成長情形，形塑互動為最大特色。
### 二、使用說明：
#### 系統要求：Windows 10
#### 第一步、[請點此](https://github.com/darren-k-chen/ECPayHappyFarm/raw/main/Statics/ECPayHappyFarm.zip)下載遊戲免安裝壓縮檔。
#### 第二步、將下載下來的 ZIP 壓縮檔解壓縮。
#### 第三步、解壓縮後點開執行檔 [ HappyFarm.exe ] 即可執行。

![20210307202254](https://github.com/darren-k-chen/ECPayHappyFarm/raw/main/assets/Pasted%20image%2020210307202254.png "assets/Pasted image 20210307202254.png")

#### ＊ 遊戲操作說明請參考影片連結： [https://youtu.be/DynkwhWv6bY](https://youtu.be/DynkwhWv6bY)
<a href="http://www.youtube.com/watch?feature=player_embedded&v=DynkwhWv6bY" target="_blank"><img src="http://img.youtube.com/vi/DynkwhWv6bY/0.jpg"　alt="IMAGE ALT TEXT HERE" width="240" height="180" border="10" /></a>

#### ＊ 在測試環境當中，物流狀態無法變更。故在 Prototype 當中，我們物流狀態變更採用掃描 QR-Code 的方式，取代買家取貨條碼，物流變更 QR-Code [請點此](https://github.com/darren-k-chen/ECPayHappyFarm/raw/main/Statics/setLogisticStatus/%E8%AE%8A%E6%9B%B4%E8%B2%A8%E7%89%A9%E7%8B%80%E6%85%8B.pdf)下載。

### 三、技術說明：

|項目 | 規格 |
|:--- | :---|
| Server IP Address | 35.201.168.83 |
| Server Hostname | api.happyfarm.darren-cv.site|
| Server OS / Web Service | Ubuntu Server 18.04 / Nginx|
| Frontend Dev. Env. / Language | Unity 2019.4.17f1 / C# |
| Backend Dev. Language | Python |

（評審期間，沒有意外的話我們的伺服器都不會關閉。若不幸評審期間伺服器出現問題，可參考[後端程式碼](https://github.com/darren-k-chen/ECPayHappyFarm/tree/main/Backend)建置伺服器環境，或請撥手機 0968669251 或發郵件至 kjchen@protonmail.ch 通知我們將問題排除，謝謝。）

#### 【前端開發技術說明】
#### 前端我們採用 Unity 開發，使用語言為 C#。關鍵程式碼請參照：

[HappyFarm/Assets/src/LandHandler.cs](HappyFarm/Assets/src/LandHandler.cs)：
這段程式碼主要處理物流狀態與作物狀態之連結。

[HappyFarm/Assets/src/Order/CommisionButtonHandler.cs](HappyFarm/Assets/src/Order/CommisionButtonHandler.cs)：
這段程式碼主要處理訂單建立之過程。

#### 【後端開發技術說明】
#### 後端我們採用 Python 結合 Flask 套件開發。關鍵程式碼請參照：

[Backend/main.py](Backend/main.py)：
這段程式碼主要處理與綠界後端系統之通訊交流與前端功能之支援。

#### 後端與前端對話之 API 說明請參考此鏈結：
<a href = "http://api.happyfarm.darren-cv.site/doc"> http://api.happyfarm.darren-cv.site/doc </a>
