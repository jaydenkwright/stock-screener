import React from 'react'
import { PriceProps } from './StockInterfaces'
import moment from 'moment'

const Card:React.FC<PriceProps> = ({ price }) => {
    return (
        <div>
          <div className="date">
            {price?.date ?
                <h5>{moment(String(price.date)).format("MMMM DD, YYYY") }</h5>
                : null
            }
          </div>
          <div className="card">
            <div className="open">
              <div className="columnPrice">
                ${price?.open}
              </div>
              <div className="columnTitle">Open</div>
            </div>
            <div className="low">
              <div className="columnPrice">
                ${price?.low}
              </div>
              <div className="columnTitle">Low</div>
            </div>
            <div className="high">
              <div className="columnPrice">
                ${price?.high}
              </div>
              <div className="columnTitle">High</div>
            </div>
            <div className="close">
              <div className="columnPrice">
                ${price?.close}
              </div>
              <div className="columnTitle">Close</div>
            </div>
          </div>
        </div>
    )
}

export default Card
