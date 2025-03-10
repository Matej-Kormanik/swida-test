
export enum WaypointType {
    DELIVERY = "DELIVERY",
    PICKUP = "PICKUP",
}

export interface IWaypoint {
    id?: number;
    location: string;
    order: number;
    type: WaypointType;
}

/*export class WaypointImpl implements IWaypoint {
    private readonly _id: number;
    private readonly _location: string;
    private readonly _orderId: number;
    private readonly _type: WaypointType;

    constructor(id: number, location: string, orderId: number, type: WaypointType) {
        this._id = id;
        this._location = location;
        this._orderId = orderId;
        this._type = type;
    }

    get id(): number {
        return this._id;
    }

    get location(): string {
        return this._location;
    }

    get orderId(): number {
        return this._orderId;
    }

    get type(): WaypointType {
        return this._type;
    }
}*/
