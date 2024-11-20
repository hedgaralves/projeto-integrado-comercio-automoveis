import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Automoveis = () => {
    const [automoveis, setAutomoveis] = useState([]);

    useEffect(() => {
        axios.get('http://127.0.0.1:8000/api/automoveis/')
            .then(response => setAutomoveis(response.data))
            .catch(error => console.error(error));
    }, []);

    return (
        <div>
            <h1>Automóveis Disponíveis</h1>
            <ul>
                {automoveis.map(automovel => (
                    <li key={automovel.id}>
                        {automovel.marca} {automovel.modelo} - {automovel.ano} - R$ {automovel.valor}
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default Automoveis;
