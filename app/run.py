from flask import Flask, jsonify, request
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'tradedb'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/tradedb'

mongo = PyMongo(app)

#######################################
# Candles                             #
#######################################
@app.route('/candles', methods=['GET'])
def get_all_candles():
    candles = mongo.db.candles
    output = []
    for candle in candles.find():
        output.append({
            'o': candle['open'], 
            'h' : candle['high'],
            'l': candle['low'],
            'c': candle['close'],
            'volume': candle['volume'],
            'time': candle['time'],
        })
    return jsonify(output)

@app.route('/candles', methods=['POST'])
def add_candle():
    candle = mongo.db.candles
    o, h, l, c = request.json['open'], request.json['high'], request.json['low'], request.json['close']
    volume, time = request.json['volume'], request.json['time']
    candle_id = star.insert({
        'open': o,
        'high': h,
        'low': l,
        'close': c,
        'volume': volume,
        'time': time,
    })
    new_star = star.find_one({'_id': star_id })
    output = {'name' : new_star['name'], 'distance' : new_star['distance']}
    return jsonify(output)

#######################################
# Trades                              #
#######################################
@app.route('/trades', methods=(['GET']))
def get_all_trades():
    trades = mongo.db.trades
    output = []
    for trade in trades.find():
        output.append({
            'time_opened': trade['time_opened'], 
            'time_closed' : trade['time_closed'],
            'bought_at': trade['bought_at'],
            'sold_at': trade['sold_at'],
            'position': trade['position'],
            'time': trade['time'],
        })
    return jsonify(output)

@app.route('/trades', methods=['POST'])
def add_trade():
    trades = mongo.db.trades
    time_opened = request.json['time_opened']
    time_closed = request.json['time_closed']
    bought_at = request.json['bought_at']
    sold_at = request.json['sold_at']
    position = request.json['position']
    time = request.json['time']
    trade_id = star.insert({
        'time_opened': time_opened,
        'time_closed' : time_closed,
        'bought_at': bought_at,
        'sold_at': sold_at,
        'position': position,
        'time': time,
    })
    new_star = star.find_one({'_id': star_id })
    output = {'name' : new_star['name'], 'distance' : new_star['distance']}
    return jsonify(output)

app.run(debug=True)