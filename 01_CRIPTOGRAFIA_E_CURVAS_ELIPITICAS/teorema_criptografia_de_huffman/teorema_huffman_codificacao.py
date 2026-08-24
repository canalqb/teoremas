#!/usr/bin/env python3
"""
🔐 Teorema de Codificação de Huffman
Implementação otimizada do algoritmo de Huffman para compressão de dados
"""

import heapq
from collections import Counter
from typing import Dict, List, Tuple, Optional


class HuffmanNode:
    """Nó da árvore de Huffman - otimizado para memória"""
    
    __slots__ = ['char', 'freq', 'left', 'right']
    
    def __init__(self, char: Optional[str] = None, freq: int = 0):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    
    def __lt__(self, other):
        return self.freq < other.freq


class HuffmanCoding:
    """Implementação eficiente do algoritmo de Huffman"""
    
    def __init__(self):
        self.heap: List[HuffmanNode] = []
        self.codes: Dict[str, str] = {}
        self.reverse_mapping: Dict[str, str] = {}
    
    def make_heap(self, text: str) -> None:
        """Cria heap de frequências - otimizado para memória"""
        # Usa Counter mais eficiente
        frequency = Counter(text)
        
        # Limpa heap anterior
        self.heap.clear()
        
        # Cria nós apenas para caracteres existentes
        for char, freq in frequency.items():
            node = HuffmanNode(char, freq)
            heapq.heappush(self.heap, node)
    
    def merge_nodes(self) -> None:
        """Combina nós para criar árvore de Huffman"""
        while len(self.heap) > 1:
            # Remove os dois nós de menor frequência
            left = heapq.heappop(self.heap)
            right = heapq.heappop(self.heap)
            
            # Cria nó pai
            merged = HuffmanNode(freq=left.freq + right.freq)
            merged.left = left
            merged.right = right
            
            # Adiciona de volta ao heap
            heapq.heappush(self.heap, merged)
    
    def make_codes_helper(self, node: HuffmanNode, current_code: str) -> None:
        """Gera códigos recursivamente - otimizado"""
        if node is None:
            return
        
        # Nó folha - caractere encontrado
        if node.char is not None:
            self.codes[node.char] = current_code
            self.reverse_mapping[current_code] = node.char
            return
        
        # Recursão para esquerda (0) e direita (1)
        self.make_codes_helper(node.left, current_code + "0")
        self.make_codes_helper(node.right, current_code + "1")
    
    def make_codes(self) -> None:
        """Gera códigos de Huffman"""
        root = heapq.heappop(self.heap) if self.heap else None
        current_code = ""
        self.make_codes_helper(root, current_code)
    
    def get_encoded_text(self, text: str) -> str:
        """Codifica texto usando códigos de Huffman - otimizado"""
        encoded_text = []
        for char in text:
            encoded_text.append(self.codes[char])
        return ''.join(encoded_text)
    
    def pad_encoded_text(self, encoded_text: str) -> Tuple[str, int]:
        """Adiciona padding para múltiplo de 8 bits"""
        padding_amount = 8 - (len(encoded_text) % 8)
        if padding_amount == 0:
            padding_amount = 8
        
        padded_info = "{0:08b}".format(padding_amount)
        padded_encoded_text = encoded_text + "0" * padding_amount + padded_info
        
        return padded_encoded_text, padding_amount
    
    def get_byte_array(self, padded_encoded_text: str) -> List[int]:
        """Converte string binária para array de bytes - otimizado"""
        if len(padded_encoded_text) % 8 != 0:
            raise ValueError("Texto codificado deve ter múltiplo de 8 bits")
        
        b = []
        for i in range(0, len(padded_encoded_text), 8):
            byte = padded_encoded_text[i:i+8]
            b.append(int(byte, 2))
        
        return b
    
    def compress(self, text: str) -> Tuple[bytes, Dict[str, str]]:
        """
        Comprime texto usando algoritmo de Huffman
        
        Args:
            text: Texto para comprimir
            
        Returns:
            Tuple[bytes, Dict]: (dados comprimidos, tabela de códigos)
        """
        if not text:
            return b'', {}
        
        # Reset para nova compressão
        self.codes.clear()
        self.reverse_mapping.clear()
        
        # Processo de compressão
        self.make_heap(text)
        self.merge_nodes()
        self.make_codes()
        
        encoded_text = self.get_encoded_text(text)
        padded_encoded_text, padding = self.pad_encoded_text(encoded_text)
        
        byte_array = self.get_byte_array(padded_encoded_text)
        
        # Retorna bytes e código de Huffman
        return bytes(byte_array), self.codes.copy()
    
    def remove_padding(self, padded_encoded_text: str) -> str:
        """Remove padding do texto codificado"""
        padded_info = padded_encoded_text[-8:]
        extra_padding = int(padded_info, 2)
        
        padded_encoded_text = padded_encoded_text[:-8]
        encoded_text = padded_encoded_text[:-1 * extra_padding]
        
        return encoded_text
    
    def decode_text(self, encoded_text: str) -> str:
        """Decodifica texto usando árvore de Huffman - otimizado"""
        current_code = ""
        decoded_text = []
        
        for bit in encoded_text:
            current_code += bit
            if current_code in self.reverse_mapping:
                character = self.reverse_mapping[current_code]
                decoded_text.append(character)
                current_code = ""
        
        return ''.join(decoded_text)
    
    def decompress(self, compressed_data: bytes, codes: Dict[str, str]) -> str:
        """
        Descomprime dados usando algoritmo de Huffman
        
        Args:
            compressed_data: Dados comprimidos
            codes: Tabela de códigos de Huffman
            
        Returns:
            str: Texto descomprimido
        """
        if not compressed_data:
            return ""
        
        # Reconstrói mapeamento reverso
        self.reverse_mapping = {v: k for k, v in codes.items()}
        
        # Converte bytes para string binária
        bit_string = []
        for byte in compressed_data:
            bit_string.append(format(byte, '08b'))
        
        padded_encoded_text = ''.join(bit_string)
        
        # Remove padding e decodifica
        encoded_text = self.remove_padding(padded_encoded_text)
        return self.decode_text(encoded_text)


class HuffmanAnalyzer:
    """Analisador de eficiência da compressão de Huffman"""
    
    @staticmethod
    def calculate_compression_ratio(original: str, compressed: bytes) -> float:
        """Calcula razão de compressão"""
        original_size = len(original.encode('utf-8')) * 8  # bits
        compressed_size = len(compressed) * 8  # bits
        return (original_size - compressed_size) / original_size * 100
    
    @staticmethod
    def calculate_entropy(text: str) -> float:
        """Calcula entropia do texto"""
        if not text:
            return 0.0
        
        frequency = Counter(text)
        text_length = len(text)
        
        entropy = 0.0
        import math
        for count in frequency.values():
            probability = count / text_length
            if probability > 0:
                entropy -= probability * math.log2(probability)
        
        return entropy
    
    @staticmethod
    def analyze_codes(codes: Dict[str, str]) -> Dict[str, float]:
        """Analisa estatísticas dos códigos"""
        if not codes:
            return {}
        
        code_lengths = [len(code) for code in codes.values()]
        
        return {
            'avg_code_length': sum(code_lengths) / len(code_lengths),
            'min_code_length': min(code_lengths),
            'max_code_length': max(code_lengths),
            'total_codes': len(codes)
        }


def demonstrate_huffman():
    """Demonstração do algoritmo de Huffman"""
    print("🔐 DEMONSTRAÇÃO - TEOREMA DE CODIFICAÇÃO DE HUFFMAN")
    print("=" * 60)
    print("Algoritmo de compressão sem perda baseado em frequência")
    print()
    
    # Texto de exemplo
    sample_text = "este e um exemplo de texto para compressao de huffman"
    
    print(f"📝 Texto original: '{sample_text}'")
    print(f"📏 Tamanho original: {len(sample_text)} caracteres")
    print()
    
    # Cria compressor
    huffman = HuffmanCoding()
    
    # Comprime
    compressed_data, codes = huffman.compress(sample_text)
    
    print("🗜️  COMPRESSÃO:")
    print(f"📦 Tamanho comprimido: {len(compressed_data)} bytes")
    print(f"🔑 Número de códigos: {len(codes)}")
    print()
    
    # Mostra tabela de códigos
    print("📋 Tabela de Códigos:")
    for char, code in sorted(codes.items()):
        print(f"   '{char}' → {code}")
    print()
    
    # Análise de eficiência
    analyzer = HuffmanAnalyzer()
    compression_ratio = analyzer.calculate_compression_ratio(sample_text, compressed_data)
    entropy = analyzer.calculate_entropy(sample_text)
    code_stats = analyzer.analyze_codes(codes)
    
    print("📊 ANÁLISE DE EFICIÊNCIA:")
    print(f"   📈 Taxa de compressão: {compression_ratio:.2f}%")
    print(f"   🔢 Entropia do texto: {entropy:.4f}")
    print(f"   📏 Comprimento médio do código: {code_stats.get('avg_code_length', 0):.2f}")
    print(f"   📐 Comprimento mínimo: {code_stats.get('min_code_length', 0)}")
    print(f"   📐 Comprimento máximo: {code_stats.get('max_code_length', 0)}")
    print()
    
    # Descompressão
    decompressed_text = huffman.decompress(compressed_data, codes)
    
    print("🔓 DESCOMPRESSÃO:")
    print(f"📝 Texto descomprimido: '{decompressed_text}'")
    print(f"✅ Verificação: {sample_text == decompressed_text}")
    print()
    
    # Teste com texto maior
    large_text = "o rato roeu a roupa do rei de roma enquanto a rainha de roma ria da raiva do rato" * 10
    
    print("🧪 TESTE COM TEXTO MAIOR:")
    large_compressed, large_codes = huffman.compress(large_text)
    large_ratio = analyzer.calculate_compression_ratio(large_text, large_compressed)
    
    print(f"📏 Texto original: {len(large_text)} caracteres")
    print(f"📦 Comprimido: {len(large_compressed)} bytes")
    print(f"📈 Taxa de compressão: {large_ratio:.2f}%")
    print()
    
    print("🎯 RELEVÂNCIA PARA O 1000 BTC PUZZLE:")
    print("   • Compressão eficiente de dados")
    print("   • Codificação otimizada por frequência")
    print("   • Aplicável em transmissão de informações")
    print("   • Base para muitos algoritmos de compressão")


def main():
    """Função principal"""
    print("🚀 INICIANDO DEMONSTRAÇÃO DO TEOREMA DE HUFFMAN")
    print()
    
    try:
        demonstrate_huffman()
        
        print("\n🎉 DEMONSTRAÇÃO CONCLUÍDA!")
        print("📚 Para mais detalhes, estude:")
        print("   • Teoria da informação de Shannon")
        print("   • Algoritmos de compressão sem perda")
        print("   • Aplicações em criptografia e comunicação")
        
    except Exception as e:
        print(f"❌ Erro na demonstração: {e}")


if __name__ == "__main__":
    main()
