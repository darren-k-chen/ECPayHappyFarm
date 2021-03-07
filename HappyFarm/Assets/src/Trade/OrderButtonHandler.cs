using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class OrderButtonHandler : MonoBehaviour
{
    void onClick() { SceneManager.LoadScene(4); }
    void Start() { }
    void Update() { }
    private void OnMouseDown() { onClick(); }
}
