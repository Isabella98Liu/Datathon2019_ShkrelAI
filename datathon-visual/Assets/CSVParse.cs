﻿using System;
using System.Collections.Generic;
using UnityEngine;

public class CSVParse
{
    private List<Tuple<DateTime, float, float>> data;
    public CSVParse(string fileName) {
        data = new List<Tuple<DateTime, float, float>>();
        var words = System.IO.File.ReadAllText(fileName).Split(new Char [] {',' , '\n' });

        for (int i = 1,idx=0; (i*7+4) < words.Length; i++) {
            idx = i*7 + 4;
            DateTime date = DateTime.Parse(words[i*7]);
            float closingPrice = float.Parse(words[idx]);
            float volume = float.Parse(words[idx+2]); 
            data.Add(new Tuple<DateTime,float,float>(date, closingPrice, volume));
        }
    }

}
