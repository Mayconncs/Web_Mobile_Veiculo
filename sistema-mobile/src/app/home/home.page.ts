import { Component } from '@angular/core';
import { IonContent, IonList, IonItem, IonInput, IonButton, NavController, AlertController, LoadingController, ToastController } from '@ionic/angular/standalone';
import { Storage } from '@ionic/storage-angular';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-home',
  templateUrl: 'home.page.html',
  styleUrls: ['home.page.scss'],
  imports: [IonList, IonItem, IonInput, IonButton, IonContent, FormsModule],
  providers: [Storage]
})
export class HomePage {

  constructor(
    public controle_carregamento: LoadingController,
    public controle_navegacao: NavController,
    public controle_alerta: AlertController,
    public controle_toast: ToastController,
    public Storage: Storage
  ) {}

  async ngOnInit() {
    await this.Storage.create();
  }

  public instancia: {username: string, password: string } = {
    username: '',
    password: ''
  };

  async autenticarUsuario() {
    alert('teste');
  }
}
