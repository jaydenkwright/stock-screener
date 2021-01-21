export type StockType = {
    id: Number,
    name: String,
    symbol: String,
    exchange: String,
    sector: String,
    industry: String,
    location: String,
    founded: String,
    date: String
}

export type StockInfoType = {
    id: Number,
    stockId: Number, 
    marketCap: BigInt, 
    volume: Number, 
    twoHundredDayAverage: Number,
    fiftyDayAverage: Number, 
    forwardPe: Number,
    forwardEps: Number,
    dividendYield: Number,
    date: String
}

export type PricesType = {
    id: number,
    stockId: Number,
    open: Number,
    high: Number,
    low: Number,
    close: Number,
    date: String
}

export interface SidebarProps{
    stock: StockType | undefined
}

export interface InfoCardProps{
    stockInfo: StockInfoType | undefined
}

export interface PricesProps{
    prices: PricesType[] | undefined
}

export interface PriceProps{
    price: PricesType | undefined
}