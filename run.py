#!/usr/bin/env python
"""
Glass Classification Web Application Launcher
FastAPI sunucusunu kolaylıkla başlatır.

Kullanım:
    python run.py                    # Varsayılan ayarlarla başlat (127.0.0.1:8000)
    python run.py --port 8080        # 8080 portunda başlat
    python run.py --host 0.0.0.0     # Tüm interface'lerde dinle
    python run.py --debug            # Debug modu ile başlat
    python run.py --reload           # Otomatik reload modu (geliştirme)
"""

import argparse
import sys
import uvicorn
from pathlib import Path


def main():
    """Komut satırı argümanlarını işle ve sunucuyu başlat."""

    parser = argparse.ArgumentParser(
        description="Glass Classification FastAPI Uygulaması Başlatıcısı",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Örnekler:
  python run.py                              # Varsayılan: 127.0.0.1:8000
  python run.py --port 8080                  # Belirtilen port
  python run.py --host 0.0.0.0 --port 8000  # Tüm interface'lerde dinle
  python run.py --debug --reload              # Debug + auto-reload
  python run.py --workers 4                   # 4 worker process ile
        """
    )

    parser.add_argument(
        "--host",
        type=str,
        default="127.0.0.1",
        help="Bağlanacak host adresi (varsayılan: 127.0.0.1)"
    )

    parser.add_argument(
        "--port",
        type=int,
        default=8000,
        help="Bağlanacak port (varsayılan: 8000)"
    )

    parser.add_argument(
        "--debug",
        action="store_true",
        help="Debug modu aktifleştirir (daha detaylı log)"
    )

    parser.add_argument(
        "--reload",
        action="store_true",
        help="Dosya değişikliklerinde otomatik olarak sunucuyu yeniden başlat (geliştirme için)"
    )

    parser.add_argument(
        "--workers",
        type=int,
        default=1,
        help="Worker process sayısı (varsayılan: 1, üretim için 4+ önerilir)"
    )

    parser.add_argument(
        "--log-level",
        type=str,
        default="info",
        choices=["critical", "error", "warning", "info", "debug"],
        help="Log seviyesi (varsayılan: info)"
    )

    args = parser.parse_args()

    # Model dosyalarının var olup olmadığını kontrol et
    model_path = Path("datasets/models/classifier.pkl")
    scaler_path = Path("datasets/models/scaler.pkl")
    label_encoder_path = Path("datasets/models/label_encoder.pkl")

    missing_files = []

    if not model_path.exists():
        missing_files.append(str(model_path))
    if not scaler_path.exists():
        missing_files.append(str(scaler_path))
    if not label_encoder_path.exists():
        missing_files.append(str(label_encoder_path))

    if missing_files:
        print("⚠️  UYARI: Bazı model dosyaları bulunamadı!")
        for file in missing_files:
            print(f"   - {file}")
        print("\n📝 Model dosyalarını oluşturmak için:")
        print("   1. Jupyter Notebook'u açın: jupyter notebook notebooks/GlassClassification.ipynb")
        print("   2. Tüm hücreleri sırasıyla çalıştırın (Run All)")
        print("   3. Ardından bu script'i tekrar çalıştırın")
        print("\n❌ Sunucu başlatılmıyor...")
        sys.exit(1)

    print("=" * 70)
    print("🚀 Glass Classification FastAPI Uygulaması Başlatılıyor...")
    print("=" * 70)
    print(f"\n🌐 Tarayıcıda açmak için:")
    print(f"   👉 http://{args.host}:{args.port}")
    print(f"\n📚 API Dokümantasyonu:")
    print(f"   👉 http://{args.host}:{args.port}/docs")
    print(f"\n🏠 Web Arayüzü (Tahmin Sayfası):")
    print(f"   👉 http://{args.host}:{args.port}/predict-page")
    print(f"\n⚙️  Ayarlar:")
    print(f"   Debug Modu: {'AKTİF ✓' if args.debug else 'Kapalı'}")
    print(f"   Auto-reload: {'AKTİF ✓' if args.reload else 'Kapalı'}")
    print(f"   Worker Sayısı: {args.workers}")
    print(f"   Log Seviyesi: {args.log_level.upper()}")
    print("=" * 70)
    print("\n💡 Sunucuyu durdurmak için: Ctrl+C tuşlarına basın\n")

    try:
        # uvicorn sunucusunu başlat
        uvicorn.run(
            "app.main:app",
            host=args.host,
            port=args.port,
            reload=args.reload,
            workers=args.workers,
            log_level=args.log_level,
            access_log=True
        )
    except KeyboardInterrupt:
        print("\n\n👋 Sunucu durduruldu. Hoşça kalın!")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Hata oluştu: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
