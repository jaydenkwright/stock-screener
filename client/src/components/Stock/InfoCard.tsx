import React from 'react'
import { InfoCardProps } from './StockInterfaces'

const InfoCard: React.FC<InfoCardProps | undefined> = ({ stockInfo }) => {
    return (
        <div className="infoCard">
              <div className="infoColumn">
                <div className="infoPrice">
                  ${stockInfo?.marketCap}
                </div>
                <div className="infoTitle">
                  {stockInfo?.marketCap ? 'Market Cap' : null}
                </div>
                <div className="infoPrice">
                  ${stockInfo?.volume}
                </div>
                <div className="infoTitle">
                  {stockInfo?.volume ? 'Volume' : null}
                </div>
                <div className="infoPrice">
                  ${stockInfo?.fiftyDayAverage}
                </div>
                <div className="infoTitle">
                  {stockInfo?.fiftyDayAverage ? '50 Day Avg.' : null}
                </div>
              </div>

              <div className="infoColumn">
                <div className="infoPrice">
                  ${stockInfo?.forwardPe}
                </div>
                <div className="infoTitle">
                  {stockInfo?.forwardPe ? 'Forward PE' : null}
                </div>
                <div className="infoPrice">
                  ${stockInfo?.forwardEps}
                </div>
                <div className="infoTitle">
                  {stockInfo?.forwardEps ? 'Forward EPS' : null}
                </div>
                <div className="infoPrice">
                  {stockInfo?.dividendYield}
                </div>
                <div className="infoTitle">
                  {stockInfo?.dividendYield ? 'Dividend Yield' : null}
                </div>
              </div>
            </div>
    )
}

export default InfoCard
