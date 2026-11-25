/* Hindi Panchang Custom Stylesheet */
body {
    background-color: #FFFEFA;
    background-image: radial-gradient(#F9EED4 1px, transparent 1px);
    background-size: 24px 24px;
}

.mandala-bg {
    background-image: url("data:image/svg+xml,%3Csvg width='120' height='120' viewBox='0 0 120 120' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' stroke='%23FF8C00' stroke-opacity='0.12' stroke-width='1'%3E%3Ccircle cx='60' cy='60' r='50'/%3E%3Ccircle cx='60' cy='60' r='38'/%3E%3Ccircle cx='60' cy='60' r='25'/%3E%3Cpath d='M60 10 L65 30 L85 20 L72 38 L95 45 L75 55 L95 75 L72 72 L80 95 L62 80 L50 100 L48 78 L25 90 L38 70 L15 65 L35 52 L20 32 L42 38 Z'/%3E%3C/g%3E%3C/svg%3E");
}

.card-hover {
    transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
}

.card-hover:hover {
    transform: translateY(-3px);
    box-shadow: 0 12px 28px -6px rgba(230, 108, 0, 0.16);
}

::-webkit-scrollbar {
    width: 8px;
}

::-webkit-scrollbar-track {
    background: #FDF8EC;
}

::-webkit-scrollbar-thumb {
    background: #FFB338;
    border-radius: 9999px;
}

::-webkit-scrollbar-thumb:hover {
    background: #E66C00;
}