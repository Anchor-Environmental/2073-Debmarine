raw_data_depth_array = [0.4940249, 
               1.541375,
               2.645669,
               3.819495,
               5.0782242,
               6.4406142,
               7.9295602,
               9.5729971,
               11.405,
               13.46714,
               15.81007,
               18.49556,
               21.59882,
               25.211411,
               29.444731,
               34.434151,
               40.344051,
               47.373692,
               55.76429,
               65.807266,
               77.853851,
               92.326073,
               109.7293,
               130.666,
            ]

delft_depth_array = [13.0666,
                    26.1332,
                    39.1998,
                    52.2664,
                    65.333,
                    78.3996,
                    91.4662,
                    104.5328,
                    117.5994,
                    130.666
                    ]


prevVal = 0
for value in delft_depth_array:
  selectednum = [num for num in raw_data_depth_array if prevVal < num <= value]
  print(selectednum)
  prevVal=value



