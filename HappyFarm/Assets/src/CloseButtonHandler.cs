using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class CloseButtonHandler : MonoBehaviour
{
    void onClick() { SceneManager.LoadScene(0); }
    void Start() { }
    void Update() { }
    private void OnMouseDown() { onClick(); }
}
