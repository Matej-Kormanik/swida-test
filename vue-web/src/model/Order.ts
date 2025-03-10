import type {IWaypoint} from "@/model/Waypoint.ts";

export interface IOrder {
    id: number;
    number: number
    customer: string;
    date: string;
    waypoints?: IWaypoint[]
}

export class OrderImpl implements IOrder {
    private readonly _customer: string;
    private readonly _date: string;
    private readonly _id: number;
    private readonly _number: number;
    private readonly _waypoints: IWaypoint[];

    constructor(customer: string, date: string, id: number, number: number, waypoints: []) {
        this._customer = customer;
        this._date = date;
        this._id = id;
        this._number = number;
        this._waypoints = waypoints;
    }


    get customer(): string {
        return this._customer;
    }

    get date(): string {
        return this._date;
    }

    get id(): number {
        return this._id;
    }

    get number(): number {
        return this._number;
    }

    get waypoints(): IWaypoint[] {
        return this._waypoints;
    }
}
