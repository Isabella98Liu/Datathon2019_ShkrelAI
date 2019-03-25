using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Orbit : MonoBehaviour
{
    private float xyPos;
    public float rate;
    public float radius;
    public Vector3 origin;
    public bool CCW;

    // Start is called before the first frame update
    void Start()
    {

    }

    // Update is called once per frame
    void Update()
    {
        if (CCW) {
            xyPos -= Mathf.PI / 3.0f * rate * Time.deltaTime;
        }
        else { 
            xyPos += Mathf.PI / 3.0f * rate * Time.deltaTime;
        }
        transform.position = new Vector3(origin.x + radius*Mathf.Cos(xyPos),origin.y + radius*Mathf.Sin(xyPos), transform.position.z);        
    }
}
