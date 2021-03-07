using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class TradeButtonHandler : MonoBehaviour
{
    void onClick() { SceneManager.LoadScene(3); }
    void Start() { }
    void Update() { }
    private void OnMouseDown() { onClick(); }
}
