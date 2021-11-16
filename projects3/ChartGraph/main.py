import database
import get_raw_prices as getPrice


# 関数の作成
def func1():
    print("function")
    
def CreateDatabase():
	database.CreateDatabase("test.db")
	database.RunQuery("test.db","create_raw_price_table.sql")

def GetPriceData():
	# 実行
	params = getPrice.get_raw_price(1301,1)
	for param in params:
		print(param)
	getPrice.raw_prices_generator(range(1301,1301))
	getPrice.insert_raw_prices_to_db("test.db", range(1301,1302))

#メイン処理================================
print("select application input num")
print("0: createdatabase")
print("1: get price data")

inputvalue = input()

# 入力番号にて処理を分岐させます。

if inputvalue == "0":
    CreateDatabase()
elif inputvalue == "1":
    GetPriceData()
else:
    print("usage")
    print(inputvalue)



