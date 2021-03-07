# ECPay Competition Team Prototype Reference
## 產品發想：開心農場
### 一、產品特色：本遊戲透過「競價模式」串接金流，提供作物集合競價的平台，使得賣方能夠脫離盤商剝削，買方也能獲取公平之價格，創造買賣雙方雙贏，並將「作物成長」結合作物運送之物流，依據物流狀態來決定作物成長情形，形塑互動為最大特色。
### 二、使用說明：
#### 系統要求：Windows 10
#### 第一步、點選以下連結下載遊戲免安裝壓縮檔：
<a href = "https://github.com/darren-k-chen/ECPayHappyFarm/raw/main/Statics/ECPayHappyFarm.zip"> https://github.com/darren-k-chen/ECPayHappyFarm/raw/main/Statics/ECPayHappyFarm.zip </a>
#### 第二步、將下載下來的 ZIP 壓縮檔解壓縮。
#### 第三步、解壓縮後點開執行檔 [ HappyFarm.exe ] 即可執行。
![[Pasted image 20210307202254.png]]
### 三、技術說明：

|項目 | 規格 |
|:--- | :---|
| Server IP Addr. | 35.201.168.83 |
| Server Domain Name | api.happyfarm.darren-cv.site|
| Server OS / Web Service | Ubuntu Server 18.04 / Nginx|
| Frontend Dev. Env. / Language | Unity 2019.4.17f1 / C# |
| Backend Dev. Language | Python |

#### 【前端開發技術說明】
#### 前端我們採用 Unity 開發，使用語言為 C#。關鍵程式碼請參照：

[HappyFarm/Assets/src/LandHandler.cs](HappyFarm/Assets/src/LandHandler.cs)

[HappyFarm/Assets/src/Order/CommisionButtonHandler.cs](HappyFarm/Assets/src/Order/CommisionButtonHandler.cs)

#### 前端我們採用 Python 開發。關鍵程式碼請參照：

[Backend/main.py](Backend/main.py)
