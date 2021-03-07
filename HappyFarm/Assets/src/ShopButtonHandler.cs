using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class ShopButtonHandler : MonoBehaviour
{
    void Start() { } void Update() { }
    private void OnMouseDown() { /*onClick();*/ } void onClick() { SceneManager.LoadScene(2); }
}
