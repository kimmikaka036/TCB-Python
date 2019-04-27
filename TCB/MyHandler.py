import base64

ata ="/9j/4AAQSkZJRgABAQEAAAAAAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAD6APoDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwD5/ooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigBaKK6zwx4OXxFp8t018YDHL5e3yt2eAc5yPWpnUjTXNLYcYuTsjk6MV6OfhanONXP/gP/wDZUqfCtZG2rq7Z/wCvf/7Kuf67Q/m/BmnsZ9jzeivRm+F6KTnV24/6dv8A7KsTXvCEWitCg1BppJe3k7cD1+8auOLpSfLF6ilSlFXaOToraXQSy7jOQMddn/16lXw1vjLC5PH/AEz/APr1brQW7MzAorcOhIoO65fP8IEfX9artpJWQIZGyemEzn9aFVg9mOxl0Vsz6GIAN1wcnts7/nTrfQvOZgbjbjuEz/Wm6kUFmYlFdJL4YSILm8Yluf8AVdB+dSQ+EhMF23hyecCLt+dJ1oLVsLHMUV0D+GNkRc3ecHGBH/8AXqCPQRIxH2gjH+x/9ehVoPqKxi0tbb+HmRwPPJQ/xBP/AK9WJPC4j8v/AEsnf/0z6frTdWK6gc3RWq2kgXQh81sf3tn/ANem3mli1mWJZWkYjJ+TGP1pqSYk7mZRV28sTaRxMX3GTPGMYxj/ABqlVJ3GFFFFABRRRQAUUUUAFFFFABRRRQAtep/DI40K7/6+T/6CteWV6l8M/wDkBXX/AF8n/wBBWuTG/wAFm1D4ztvxpqsUOQaU+9IRXhHaOaXKLGuAvU15f41uHuNee3Qn5FC8dq9LYhFJPAHJrzx9J1DUNVmuzazASOTuIxgV2YW0ZczOevdqyMa0tr7CpG7lRxz0NbERvcC2REV8c8Hj8a149DmjXMs3lIPTqadGvlbmwAnYdzXROqpbHPytIwZIGtnJnYbyPvdajjni8zMSfvMbXcjnFa99bvdSxLHF5jjJYjtT4fD7syM7hEB69SaVNu4JNnNtD5zkFiCQSvtWjp9uot1lbJB+9XQR6BZQuTIzFPRRU/8AZVqISsG4IW5Df41s9R8rObuWAV7mQYQcKP5CrGiidImM5Ilc52/3R2q9LoKveLJNcLIi/cRT/Sr62ixyBgp56t61nVbUbDcdDPtLSOdSkoBznr2OawnltbWSWCZ9sqsR7V0UivDJOFAGDnn3rV0zwfY63oL3NzEqXEh3BwfmUdjUUrKepCi2eevfx+WSHII5G0c0PqImVQN6MOuRWtquk6lbObeWwMoUfJOkZBIrGuNFuIoGfc0cin5o2HNdq5GEouIRBPtSN5m4g88c4pDIGaSdiXaQ/p2qr9nnCKXJQHs3Wl3A/dB44xVuy2IsytrDvLDbSP1Ytx2HQVj1ta0pWysC3DHzMj05FYtaQ+EYUUUVQBRRRQAUUUUAFFFFABRRRQAtep/DH/kBXX/Xyf8A0Fa8sr1T4Y/8gK7/AOvk/wDoK1yY3+Czah8Z2rUmB69KUjmkIrwjtGU0+maftzTGHXsR19hVK70QtDG1p3DxBBkHtUUNiZSu6QBQM4xnJrQeNLiVdqAlR95ugqUstuf3eWc8E4wK76NPS7OecVKVyotiqybdhQE5JHU/Wr4a1tlwZkB/ugZrFvLlmb77Hd1wetUYZXeYxqvPYg9K35GJaHTNe2xGVRVb35J/CopCzNlpNqeijk1QiiEJ3HBfuzHmrsex1ZvMSRgOeatbhqIBAxwM49xnmnpbyD7pyndTnBpqBchVJVz/AAHofpUyNJbAu3MecMPQ1TimLUjfTopCWLkbjyDzk1r6ZPLaRCOKKNivBXpkVWWRA21sbWGQavNEDaiaI/KepU8is5U77AtGT32sw2ypJfxrBGTgEsK4HXLzT7nX52DRvbbQwCHO44rI8TW7W+rv9rupZd3zJnJwPasbfAQJB5zNnrt6URptdSZyvuia7sLpVM8ioEznBPIHpVeLyQhJBDVfKPfRqJPPwOhY9B64qXVNNW0ljS3QyJtBMg5BqubuNRjJHPa8wNpYjcC/7zcPTkYrBrZ12MoYMgjO7r+FY9dVN3ijKSs7CUUUVZIUUUUAFFFFABRRRQAUUUUALXqnwx/5AN3/ANfJ/wDQVryuvVPhj/yArv8A6+T/AOgrXJjf4LNqHxnak9Kack0p96CK8NW6ndYYx/Kqk7ncqkfJn7mcbvrVxFaSeOMNgHk+uKSa0ZrhSVABHG6uuhBfEYyepJHGiW+Qn3ugqrdW8ef3is7EenA+lasVs2QTyB90f57VUkQTTFm5jU4GD1Ndl7CUbnN3FuzvwOOihR1qxDZRWEIZ+Zm5wBk4rYii3zM4QADgLVi30/eTLNguaHUNFTuc+sEszb/swYemSDViGwjDhmgZG7kZrqUs41AIAwevFTJBGF5XP60Rncr2Rz39mAgMDvU9B1x/hSpFLHLh/nDcEt0Yeh966NbONvmhIBPUY61FNZGTgjOfbvV8xDpM5plaJmQjdGTlT6VPZTukTwspZW+ZeOh9K2H05ChGNpx6VGbWKJdq/eAocheyZxOrKl3MFkTdnIXPUGuX1K0nsGysYAPKs3WvQtW0r7RG1wg+dBk7Ris65shrPh5uAZoDwuOc1cJGM4NHnP2+/Ryy43H0Xr7ZpU1a7RSrKDx0DHFacFhJK7xqhIX7xPQD3qpd6e8D8M2OvSqco7GST3MXVrz7UsAKMpQNwTnrisqtHU1CuhBznNZ9bx20IbuxKKKKYgooooAKKKKACiiigAooooAWvUvhn/yArsf9PJ/9BWvLa9S+Gf8AyArr/r5P/oK1yY3+Czah8Z2x5xg/WkLL6mlJ6DHPakPp3rwztLWn7Q+8AFidv0rReFXvC7jlR0xwKz9PDIySEDAOcVpSysIWIUkyOBgV6FP4TFjrpClqSp5fhTWVJGRb4O0Y6YNbGoPmCAKCSFxjtmqCQ7gVZPl71pJm1KNyvCnlwAKp9yO9aUICDBA5GRxnFMijOQowTxkelWUUlT2qFqb2HowxyCD9MU5QMkqAG9+9NdUwMH86aABllJJ/KtIqwD2DKdxjYH1WmiaPbyzDBzzxQWYruDE+zUxZsgho23duKoQA7yzRljjtVWUHdltp7YNSA3LMxJwB2x0qKbkAuisp6+1ITEwqho/b8KxrGFotSkgThZe3vWrgY+XcV6YznFUZcw6hFKByGHNOOjMJq6EuLC2srS5dY1UydV29a5XUbBb2IY4cdDXa+JJJI7JPlyj8ZrkC5BOK56t1PQxhsec+J7J7KaBXXG4Nj9K5+ux8effsfo//ALLXG16dBuVNNnPNWkFFFFakBRRRQAUUUUAFFFFABRRRQAor1P4Yn/iRXX/Xwf8A0Fa8sFeo/DM40K6/6+D/AOgrXJjf4LNaPxnbHk1btYlKFnT5uxNVonVZAXGQK0GuFEeRls9AB0rxEtTutcLULuJJ5QEj0qSS68uEbsblzgfWqD3eyEFSPmODxzShi6eZ09Cea9GF1EztrYuh3lwGbGBzUscmU4wuD371UgBLAMnPXrVpiCARgD1AqW7s6VFJDZ7oW4bauWYZwehNV7bUrosS0RxnlWGM/SripE6CSbDZPHaph5Tg7MFemM8irjFCu+ghuVZRiMAnnOelIsjsAXwB2x0NRNEse4r36k0w5IChsKvSrFdl5NxjAUZ55p7AqMNjpnimxS+VCe+R3FLJOixhnHz7ehpmilpqQPKgBBOO4BPaopEDHKnORwKy72+Xf9zdnr9KikvZHiHlqxGMfJxinFIylM11jyFP3WHUVTvI90sYOdxYYGO9Y1vqk1vdfMWPruQ81rSyebbCfaQd479KVrMzbuhviOYNDFGQcLyR6GuYZVHTpXUa68ciRSEDzHGef4q5x1znjFYVviMo7HCePPvWGPST/wBlrja7Lx6VMliFPQP/AOy1xtejh/4SOap8TEooorYgKKKKACiiigAooooAKKKKAFr1H4aD/iRXX/Xwf/QVry6vUvhmD/YV3j/n5P8A6CtcmN/gs2ofGdmFJbAJ54xWlEkpljihRFQHG5+rH2qrZpvuowex6VraYRNcxqwOY8kYHfNeXRSauelSWjGXVpGVPmoEdDk1VRkVd+0nsvpWvfxrgylcqwIbvWAZTNN5bAqF6LjFda0RFRO9y1EwY5GPUjPSrqw7yhGQB/dqnACCDjLVqwMFHIrLdmr2MzVX+ywbypb0Uetc9d65cafcLBJaOXC7m2c7R711t1Gl2jKWAx0FcxfeF47u6Mz+a7YwQsm0MfXFdFPl6mbUujLI1qdIo2kgZY5lyjk5GKlhu23gK2VNNa2mS1gt2j2QwDCgGrNt5fllI4wWPVsVcmrAk+prwqZ7YHnHpWRr18tvNHaR5aRh0HUCr0MrxYUnisTVot2pPMcGR48Kc9MVMSpaIfaiztlzfSfvMZC5qyb20kOICgA9etcdqNrcvAvlRGSZSTIA+OKk0Gy822uTfQ+UC37nJO9fx7itFHQwuzpZDCd6uq4IyDVfcV0yUMcZORgYqpZW1zt8ueRpB/DnsKmvS0MRU/dBrJ7g0Mvrnz4bdRnCjaQeorJvlkjhaUMTGgyVUckVoyyguE8jLnBLf3arXi3fljyduMc4PJrKorTuQ43R5z4vuILkWTwMGGHz7dK5at3xLbm3vgCMZycflWHXpUbciscUlZ2EooorQQUUUUAFFFFABRRRQAUUUUALXqXwz/5AN1/18n/0Fa8tr1T4YjOhXf8A18n/ANBWuTG6UWbUPjO4tX8u5jf0bGa07ING87ljlfSsK+dorYuvUEGtm2uQ0byYDF4gw7fUV5VDselTe4y/U3bRgyMu05xnGT2qrtKz7vT3q0W+VZHR1Y8AAZFMmixN9e9dctymTQSLvGT1OK0lQ7ASeDWXbf6wA4LDv6VsxbXGSeBWaWoFVrXLhvTtSMxTjj8FzVzKknGPXpUXkktvYH8q1jEdig0E94SGJCDjb0NS/ZUgjCjG0DtViW5S3UAjB/Ks57s3UhjTPXqKppisPmdmiJUDHpVW4hRrVQSd4OcnnFSOhQEOTj1qnMSqHa2QOQDTSYTs0KYIZYyk8X70dCv8QqIabEDuDMR6bq0TCWiQuMEjIxUBUx5JyccUNszsPQbAPl4AxWbquApBwVPNaSyrkDsay9Ybe3lrx8nB96SWpElYgt41e73MpYNjgHpnvVy8tBbuADkdjUdpmK4TjIVBxWvdwm6XKrgkjgelYV3dktW0PHPiLbGG8tJMcSB8H1xiuJr034uosb6QijGFl7e6V5lXp4f+EjhqfExKKKK2ICiiigAooooAKKKKACiiigBa9U+GP/ICu/8Ar4P/AKCteV16p8Mc/wBg3eDj/SD/AOgrXJjleizah8Z2F9AzWjhgRkZFWvDnl31msTNl4ht298etRuzMjKSTxXP2093Z6mXswxlDYCqM5FePTlZndGVj0gZZhFGo2454rInH745OCP51WGq67NAB/ZhWQ/xHirEJd4w0y4k/jUetdhpzJ6Iji+W4Gec962ogNnrWNtIvFHbr9K2UBbbg8CnFO401sTJGAR2FR6hepa2+d2MDnmnTSrFGxJxiubklOqXWQf8AR425wfvGtog5WGl5rhXuJA208Kvt60+01C2ifbtbH98rxn61b85SpwPu8ADtTfLRoSeh7gUOVxORZN3C1uweNSTjDehrLvLuOA9Bz1Lds1VNnLl/IkO0HKhqzZbSWWcG4kB/lVRehDmb2k36XcbQ7sFTgZ9KtSqpBHUZ4rCtEWC7i2EDPymt2RWjPzAZz296bsVHVFYptcHPzHqT3rFv5P8ASjtUnJArancBS3HHrWTEWe73gAt15rPrciRYh5usdOAM1vISmNhOf4axxBslVgc7mrUywyDwB/FXLWfvEz3PMPjCxaXSC3J2zZP4rXmFek/FtNtxpbb2bcsvDduVrzavUw38JHBU+JiUUUVuQFFFFABRRRQAUUUUAFFFFAC16p8Mf+QDdD/p5P8A6CteV16r8L136HcrnGbrH/jq1y4xXotGtH4j07TNEM8C3t2NtpnCjoXP+FacKQFZJbe1jSNBjcq8/nWt4iiFtoFnap8o+VePaobeJI7Hy+m7rWdCjGKRrzcxBalhAzu2QTxXPAnz5lzzuP8AOugvZEiiMcbDjr7Vy8cpa4d88FzVVrcqNaO7JWGLxWKjOK1IXBb52xxwuKzWAN0jdqtI2TgE+/0rBGxT1QyXEyWqNsRz8zegqrLJa2m2LeoA6DOKuX7+XcRLGcswxyKorpML3Pmyr5pxgM4zg1XMkO1x41SzHyebHwOlSDULNwVW5i57bqjbTrYbiYwP90YqnNpVgzZO0H1wKcbMpRVi558aYAkjx2+YVQkkVmJwCD0BFU5tEs3JHm5x9RUE2kKgH2e6ZTnjknn6GrsiZJFuXiJmH3lI6VvxSfaLCKQcEjkHrXJ6fb3kepSPczEjbgKv3T711FiDFpLKRllc9alkx0KV+4jhb34qlaTKjNnrkVJqLByqBueprG1TUY9JhaQkM5+VF9TWU200kQ3bU15dZtLORZLtwmCcLnr+FVm8awOxFvbhVXq0rYH5V57c3xu2LyNl85Lf4VHDbTXrADOwnrQqKbvI5J1ZN6B471r+2Lu1IwViD4YZwc49fpXH10nimxWx+xIHQsVYlVOdvTrXN16NKKjBJGTberCiiirEFFFFABRRRQAUUUUAFFFFAC17T8FdHl1fTrlUJWNLvLt6DateK19Jfs4xqfCerPj5vt2Pw8tazqw542KjLldz1TVNPTUdL8sg+bF8yH0YVyzfJHvluREoHsP1Nd2o2yt6NXlHjzSJrDVfPjyba45X0Vu4rL4Ua0tXZlPVNXgWUw2bNKM4eVjx+FMs1DlhnOOlYpOyIgL0HXtWvpbEWyseMiuWcnJ3Z3QgkXmx5iDHf8qsgFCNpyB1qrcj5Uk7McfSrcEgngByN2KSG1YqPDJJdGdyQF4XPSpwdoAx+NIXIcB+DnmiZieV4x0poOYQyKUK9CD2qhLaqzgkAZ/OrADE4IA/rSjO9SwIHbNOCDmKBskCkE9e9OS1iUqcZPUVafGeKq78M3tVOPmJuxHdKixlwPmXmrU1wFs1VAASASM9zVKU5UhujdabFGWaOIEMCcAkdqErEcxVmO5yw5xXGeLpxJcRRFgdg5GO9euyeD0lR/KmKTj1GVJrzLV/Bmvx6jNPc2DzruJHkncMdqlU5c/NI5qk9NDkra0BHmTZEf8Ad7mtGG/WLKx4AIwParz6Nf3JWNoBb44/efw/hV0aHp2lwLNdAzOT8uTxn6U5TtuzFQfbQ4XxBBKnkTSKQJS5Ut1OMc1h113je6Ny1jgKI0DhABjH3a5Cu2i7wTJdr6BRRRWggooooAKKKKACiiigAooooAK+kP2cZUHhnVody7zebtuecbF5r5wr3z9ne8so01C0PF7JIWBx1QKvGfrmkyoq578w7+lUdW0uHV9OltZxw44PdT6ir+cilAwMVLiJSa1R8+arYz6deS2cwIMbEE+voa0dJkD2oV8AoOQa7/xz4b/tO2W7t4C1xH97b1Za86SNrZ13LhhwysCDj3Fck6dmelSqKSN3KSQgYBU9KzDK9rKUJ4zwatRTq6BY17dAKJF81WR1GPWsUrM0euxCZXkUsvBH8Q5zTVulYbWOM9c1WLtbSbSCVHSlkdJvnQc1RnYseeY3I3gH07YqGW5ZmOTuPsai+zFlwpwfQGopIpgMByB7VcWhak7XAxgkZA6VCZi4HQmqjJKXOWx74oVjnGSavQTbJ3Ikm27uMcmr+ktHNrENsg3bP3knt6VngJDGZGPStvwbZtdXDXQH+ubgnsBTjFNkSvY0PE/iGbwtr9ndTR+bYXUYWRFPzKw/iH4V1lneWmoWkVzbPHPbyLuDjnP/ANeode8NWevWEcFzEsjx52k9QfY15x4Z1geEvF9xodw0i6bNJtXzR9xz0INb2EoRqQ0+Jfieny6ZYXI/e2UL/wC8lZOo+B9B1Uq01q0bqMBo5CMfh0rqlTPOB/jS+WMdKHTTOW/Q+afjN4WsvDEujJZSSsk6zEiQg4wU/wAa8q717n+0au2fw4fVLj+cdeGVcUkrIlhRRRTEFFFFABRRRQAUUUUAFFFFAC969Y+EGtPojtOY4vIluQjyP8u3gdG/HpXk9fQnwK0W01nwJqsV1AkqG/IIb08tOlJm1GUYy97Y9zikSaJJI2BRhkEHORU3as7SrH+zrNLVWYxRjCA/wj0rQOdnHXtT3MmknZEUsoQhP4m/IVzWs6tYWV+6S6Q92YVD3EiRqxiU9GweSPpXTxphfnwWPJNQXmm2d+oFzbxy46EjkfjUuN9gTsZd3pOna7pSvBEib03QyooUj0rza+t7zT7h4LxDHIDtBwcN9DXskcaRoERQqgYAHaq9/YW2oWz29xGro4wcjpWc6fMbUqzg/I8SmZmbngdxT4ovl3dRVvW9Ln0bUntJwSvWJ/7y+tV/MRbUsGB7c1zSWtjtUotXQ+ORVVhnGfSmMwccdPU1lC4maXfGxxnHAzV05kUDI56gGiwkhk3CkYBPtTIIWzuK8elTIi7/AGHWpR84IXOPpTvYdkZ91FJM3lx5JJxgDqa9C8G6PJbWgUKWCr95jgg98VieG9Ke7vA6LhVOFJ9e5r0y3gt9JssSvGiKMs7HFa00c9aS2Q9UkEKgj7pyT3rkfiJoP27Q7i6trRZrkL8oC/N/vCukTXYblGFnDLL6OUwpqhcy6hdRNE06KjDGI0yf1ra5hCTjJS7Gb8P9ek1rw1F9oP8ApNsfIlz1OOh/Kuvx+Nc54f0KHSrm8uIw/mXRBkJ6Ej0HbrXQwn5tvpVXHUacuZHg37SX+v8ADf8AuXH8468Ir3n9pX/X+Gv9y4/nHXg1MyYUUUUCCiiigAooooAKKKKACiiigAr6V/Zzj3eC9UYcMNRPP/bNK+aq+mf2b/8AkSdU/wCwif8A0WlAHsnPenUUUAFFFFACHrVLUdRtdMtxPdybELBBwSSx6AAVdNZOu6RJq9kkcNwbeeKQSRyYyAR2I7ik720AzfEGm23iXTm+zsDd2/zIO49iPevIr93YtbkMojzv9R7V7NoWgz6XcXl5d3Yuby7K+YyrtUY6YFcb470AQX/26FcR3PD4HRx3/GueUdLvc6aMteXocHAjGEB5duTyi8HFa8Wnz7f3bK4PQnrUUNjypPJ9TW4kYjhGW21nNrodkYszksWRv3rbXI6Zp8UEl3ewWFqgMkhxx0A7k06eQklh87DofSu28IaAthZnULkYuJhyxHRfQURg2yaslBGvplhDpFkDs+4ML7mq13bG/fzLkGQ/woeg/CtVkad/MY4UDhKlgtwG8xhwPuiutRsee227soRwGC32BcDHHtV6zjXyQdiketOdTJIB2zVhE2LgDAoSFcidVUHFRQZZycfSrEo+U+tQ2x5NN7j6Hg37Sv8Ax8eG/wDcuP5x14NXvX7S3/Hx4b/3Lj+cdeC0yAooooAKKKKACiiigAooooAKKKKACvpn9m//AJEnVP8AsIn/ANFpXzNX0z+zf/yJOqf9hE/+i0oA9mooooAKKKKACiiigBMVR1XTo9T06a1k/jX5T6Hsav0jfdNJoFoePS20kE5ilJ3xkqQaexDps9fUVo+If+RlvP8AeH8qzX+9XFJWlY9OnJtJmt4Y0EX9z58i/uoT0P8AEa74xEhQgGxeFFY3hP8A5Ah+proI/wDVr9K6KasjjxEm5MURgLjv3NJIdicU8dBUVx1WtTFBCmV3HjPapsUkf3BTjTQiGYfKarW/3iDVuX7pqpF980nuUjwn9pb/AI+PDX+5cfzjrwWvev2lv9f4a/3Ln+cdeC0yQooooAKKKKACiiigD//Z"

print(base64.b64decode(ata))