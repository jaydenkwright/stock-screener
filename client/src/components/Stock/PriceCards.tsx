import React from 'react'
import Card from './Card'
import { PricesProps } from './StockInterfaces'

const PriceCards: React.FC<PricesProps | undefined> = ({ prices }) => {
    return (
        <div className="priceCards">
            {
                prices ? 
                    prices?.map((price) => (
                        <Card price={price} key={price.id}/>
                    )) : null
            }
        </div>
    )
}

export default PriceCards
