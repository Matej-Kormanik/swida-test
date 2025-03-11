
export function formatDate(isoString: string): string {
    return new Intl.DateTimeFormat("sk-SK", {
        year: "numeric",
        month: "2-digit",
        day: "2-digit"
    }).format(new Date(isoString));
}
