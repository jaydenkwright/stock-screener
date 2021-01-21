import React from 'react'
import { SidebarProps } from './StockInterfaces'

const Sidebar: React.FC<SidebarProps | undefined> = ({ stock }) => {
    return (
        <div className="sidebar">
            <div className="stockSymbol">
              <h1>{stock?.symbol}</h1>
              <h3>{stock?.name}</h3>
            </div>
            <div className="stockInfo">
              <div className="infoItem">
                <h2>{stock?.exchange}</h2>
              </div>
              <div className="infoItem">
                <h2>{stock?.industry}</h2>
              </div>
              <div className="infoItem">
                <h2>{stock?.sector}</h2>
              </div>
              <div className="infoItem">
                <h2>{stock?.location}</h2>
              </div>
            </div>
          </div>
    )
}

export default Sidebar
