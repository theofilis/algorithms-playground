from nosdynamic algorithme.Alignment import edit

class TestAlignment:
    def test_strings_to_numeric(self):
        x = ' exponential'
        y = ' polynomial'
        a = edit(x, y)
        for i in range(len(x)):
            for j in range(len(y)):
                print(a[i,j], end=" ")
            print()