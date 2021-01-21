import React, { useState, useEffect } from 'react'
import InfoCard from './InfoCard'
import PriceCards from './PriceCards'
import Sidebar from './Sidebar'
import axios from 'axios'
import { StockType, StockInfoType, PricesType } from './StockInterfaces'

export const Stock = () => {
    const [stock, setStock] = useState<StockType>()
    const [stockInfo, setStockInfo] = useState<StockInfoType>()
    const [prices, setPrices] = useState<PricesType[]>()
    const [error, setError] = useState<String>()

    useEffect(() => {
        const getStock = async (symbol: String) => {
            try {
                const res = await axios.get(`http://localhost:8000/api/stock/symbol/${symbol}`)
                setStock(res.data.stock)
                setStockInfo(res.data.stockInfo)
                setPrices(res.data.prices)
            } catch (error) {
                setError(error.response.data.detail)
                console.log(error.response.data.detail)
            }
        }
        getStock('goog')
    }, [])

    return (
        
        <main>
            {!error ?
            <section className='glass'>
                <Sidebar stock={stock} />
                <div className="content">
                    <InfoCard stockInfo={stockInfo} />
                    <PriceCards prices={prices} />
                </div>
            </section>
            : error}
        </main>
    )
}

export default Stock
