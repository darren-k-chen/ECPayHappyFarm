using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class DealButtonHandler : MonoBehaviour
{
    void onClick() { SceneManager.LoadScene(6); }
    void Start() { }
    void Update() { }
    private void OnMouseDown() { onClick(); }
}
